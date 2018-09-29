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
    def data(self):
        return self.__data


class CarSelector:
    def __init__(self):
        self.__car_list = None
        self.__car_description = None
        self.__cars = list()

    def set_car_list(self, car_list):
        self.__car_list = car_list

    def set_car_description(self, car_description):
        self.__car_description = car_description

    def read_cars(self):
        for car in self.__car_list['rentObjects']:
            c = Car(car, self.__get_details(car))
            self.__cars.append(c)

    def __get_details(self, raw_car):
        return [d for d in self.__car_description if d['id'] == raw_car['classificationId']]

    @property
    def cars(self):
        return self.__cars


connector = BmwRent()
connector.login()
connector.load_data()
connector.write_to_file()

car_selector = CarSelector()
with open('car_list.json', 'r') as f:
    car_selector.set_car_list(json.load(f))

with open('car_description.json', 'r') as f:
    car_selector.set_car_description(json.load(f))
car_selector.read_cars()

