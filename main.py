from datetime import datetime
from colour_print import *
from application.salary import calculate_salary
from application.db.people import get_employees


def date_now():
    today = datetime.today()
    print(today)


if __name__ == '__main__':
    pg("Date: ")
    date_now()
    py(get_employees())
    pb( calculate_salary())
    pr("Red")
