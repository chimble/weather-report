from tenday import Tenday
from currentconditions import Currentconditions
from alerts import Alerts
from hurricane import Hurricane
from sunriseset import Sunriseset


def main_menu():
    while True:
        choice = input("""
        what do you want?:
        (1)CurrentConditions,
        (2)TenDayForecast,
        (3)ALERTS,
        (4)Hurricanes,
        (5)SunriseSunset,
        (6)EXIT\n\n""")
        if choice == '1':
            c = Currentconditions()
            c.curr()
        if choice == '2':
            c = Tenday()
            c.ten()
        if choice == '3':
            c = Alerts()
            c.scaryboys()
        if choice == '4':
            c = Hurricane()
            c.windy()
        if choice == '5':
            c = Sunriseset()
            c.sun()
        if choice == '6':
            break
main_menu()
