from __future__ import print_function
from app.model import CarDiffCalculator
from datetime import datetime
import smtplib
import os

def OnNewCars(set_of_new_cars):
    lines = list()
    print('Sending email')
    lines.append('Folgende Autos sind neu buchbar:')
    for new_car in set_of_new_cars:
        lines.append('- {}'.format(new_car.name))
    lines.append('Viel Erfolg beim buchen')
    message = 'Subject:{subject}\n\n{body}'.format(subject='Neue autos bei bmwrent', body='\n'.join(lines))

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('bmwrentnotification@gmail.com', os.environ.get("EMAIL_PW", ''))
    server.sendmail("bmwrentnotification@gmail.de", os.environ.get("RECIPIENT", ''), message)


def main():
    calc = CarDiffCalculator()
    calc.set_callback_on_new_cars(OnNewCars)
    calc.calculate_changes()
    calc.update_files()


if __name__ == "__main__":
    print('Running', datetime.now())
    main()
    print('Done')

