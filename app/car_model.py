import requests
import re
import time
import json


class BmwRent:
    LOGIN_HEADERS = {
        'Host': 'mm-portal.bmw-on-demand.de',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://mm-portal.bmw-on-demand.de/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '0',
    }

    API_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://mm-portal.bmw-on-demand.de/index.do?action=display',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
    }

    def __init__(self):
        self.__car_list = json.loads('{}')
        self.__car_description = json.loads('{}')
        self.__station_data = {}
        self.__cookie = {}

    def post_data(self, url, **kwargs):
        if 'login.do' in url:
            headers = self.LOGIN_HEADERS
        elif 'master.do' in url or 'classifications.jsp' in url:
            headers = self.API_HEADERS
        else:
            headers = {}

        r = requests.post(url, cookies=self.__cookie, headers=headers, **kwargs)
        return r

    def login(self):
        # Obtain a session id to authenticate our request
        body = self.post_data('https://mm-portal.bmw-on-demand.de/')
        match = re.search('jsessionid=(\w+)"', body.text)
        assert match, 'No session id found'
        sessionId = match.group(1)
        print('Retreived session cookie: {}'.format(sessionId))

        self.__cookie = {
            'JSESSIONID': sessionId,
            '_ga': 'GA1.2.1366563702.1538171140',
            '_gid': 'GA1.2.1161286092.1538171140',
            '_gat': '1',
        }

        response = self.post_data('https://mm-portal.bmw-on-demand.de/login.do')
        if 'form name="FormBeanLogon" method="POST" action="/login.do' in response.text:
            raise Exception('Login failed!')

        print('Successfully logged in (Anonymous)')

    def load_data(self):
        self.__car_list = self.post_data('https://mm-portal.bmw-on-demand.de/master.do?action=disposition',
                                         params={'action': 'disposition'},
                                         data='stationId=50585').json()

        self.__car_description = self.post_data(
            'https://mm-portal.bmw-on-demand.de/service/masterdata/classifications.jsp',
            params={'_dc': str(int(round(time.time() * 1000)))}).json()
        self.__load_details()

    def __load_details(self):
        html_response = self.post_data('https://mm-portal.bmw-on-demand.de/index.do', params={'action': 'display'})
        if html_response.status_code != 200:
            raise Exception('Could net retrieve response from index.do')

        in_master_data = False
        data = dict()
        data_rex = re.compile('^\s*\w+\s*=\s*[{[].+;$')
        for line in html_response.text.splitlines():
            if 'MASTER DATA' in line:
                in_master_data = True
            if 'userFieldsMap' in line:
                break

            if in_master_data and data_rex.match(line):
                key, val = [w.strip() for w in line.split('=', 1)]
                data[key] = val.rstrip(';')

        for key, val in data.items():
            data[key] = json.loads(val)

        self.__parse_details(data)

    def __parse_details(self, data):
        self.__station_data = data['stationData']
        self.__station_opening_hours = data['statHourBusData']
        self.__vehicle_detail_data = data['rentObjData']

    @property
    def station_data(self):
        return self.__station_data

    @property
    def station_opening_hours(self):
        return self.__station_opening_hours

    @property
    def vehicle_detail_data(self):
        return self.__vehicle_detail_data

    @property
    def car_description(self):
        return self.__car_description

    @property
    def car_list(self):
        return self.__car_list

    def write_to_file(self):
        with open('car_list.json', 'w') as f:
            json.dump(self.__car_list, f)

        with open('car_description.json', 'w') as f:
            json.dump(self.__car_description, f)


class Car:
    def __init__(self, data, details):
        self.__data = data
        self.__details = details[0]

    @property
    def name(self):
        return self.__details['shortDescr']

    @property
    def description(self):
        return self.__details['wwwDescr']

    @property
    def data(self):
        return self.__data

    @property
    def details(self):
        return self.__details

    @property
    def price(self):
        return float(self.__data['price'])

    def __repr__(self):
        return '<Car {}>'.format(self.name)

    def __str__(self):
        return '<Car {}>'.format(self.name)

    def __eq__(self, other):
        return self.__data['Id'] == other.__data['Id']

    def __hash__(self):
        return hash(self.__data['Id'])


class CarSelector:
    def __init__(self):
        self.__car_list = None
        self.__car_description = None
        self.__cars = list()

    def set_car_list(self, car_list):
        assert car_list is not None, 'Must be not none'
        self.__car_list = car_list

    def set_car_description(self, car_description):
        assert car_description is not None, 'Must be not none'
        self.__car_description = car_description

    def load_from_file(self):
        with open('car_list.json', 'r') as f:
            self.set_car_list(json.load(f))

        with open('car_description.json', 'r') as f:
            self.set_car_description(json.load(f))

    def read_cars(self):
        self.__cars = list()
        for car in self.__car_list['rentObjects']:
            c = Car(car, self.__get_details(car))
            self.__cars.append(c)

    def __get_details(self, raw_car):
        return [d for d in self.__car_description if d['id'] == raw_car['classificationId']]

    @property
    def cars(self):
        return self.__cars


class CarDiffCalculator:
    def __init__(self):
        self.__con = BmwRent()
        self.__on_new_cars = lambda x: x
        self.__added_cars = set()
        self.__removed_cars = set()

        self.__connector = BmwRent()

        self.__existing_car_selector = CarSelector()
        self.__existing_car_selector.load_from_file()
        self.__existing_car_selector.read_cars()

    def set_callback_on_new_cars(self, callback):
        assert callable(callback), 'Can only set a callable object'
        self.__on_new_cars = callback

    def calculate_changes(self):
        self.__con.login()
        self.__con.load_data()

        online_cars = CarSelector()
        online_cars.set_car_list(self.__con.car_list)
        online_cars.set_car_description(self.__con.car_description)
        online_cars.read_cars()

        last_known_cars = set(self.__existing_car_selector.cars)
        cars_online = set(online_cars.cars)

        self.__added_cars = cars_online - last_known_cars
        self.__removed_cars = last_known_cars - cars_online

        if self.__added_cars:
            self.__on_new_cars(self.__added_cars)

    def update_files(self):
        self.__con.write_to_file()

    @property
    def removed_cars(self):
        return self.__removed_cars

    @property
    def added_cars(self):
        return self.__added_cars


car_selector = CarSelector()
