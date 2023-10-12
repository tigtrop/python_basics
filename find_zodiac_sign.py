import pandas
import pandas as pd
from addict import Dict
from _datetime import date
from datetime import datetime

zodiacs = Dict()
zodiacs.Aries = pd.date_range(start="2020-03-21",end="2020-04-19")
zodiacs.Taurus = pd.date_range(start="2020-04-20",end="2020-05-20")
zodiacs.Gemini = pd.date_range(start="2020-05-21",end="2020-06-20")
zodiacs.Cancer = pd.date_range(start="2020-06-21",end="2020-07-22")
zodiacs.Leo = pd.date_range(start="2020-07-23",end="2020-08-22")
zodiacs.Virgo = pd.date_range(start="2020-08-23",end="2020-09-22")
zodiacs.Libra = pd.date_range(start="2020-09-23",end="2020-10-22")
zodiacs.Scorpio = pd.date_range(start="2020-10-23",end="2020-11-21")
zodiacs.Sagittarius = pd.date_range(start="2020-11-22",end="2020-12-21")
zodiacs.Capricorn = pd.date_range(start="2020-12-22",end="2021-01-19")
zodiacs.Aquarius = pd.date_range(start="2020-01-20",end="2020-02-18")
zodiacs.Pisces = pd.date_range(start="2020-02-10",end="2020-03-20")

def find_zodiac_sign():

    date_of_birth = input('Enter the date of birth (dd-mm-yyyy): ')
    result = Dict()

# input validation

    if len(date_of_birth) != 10:
        return print('The date format is wrong.')

# creating a date object from the input value

    try:
        date_of_birth = pd.to_datetime(date_of_birth, format='%d-%m-%Y')
    except ValueError:
        return print('The day is out of range for month')

    # define a zodiac

    for zod_name in zodiacs:
        for zod_period in zodiacs[zod_name]:
            if date_of_birth.strftime('%d-%m') in zod_period.strftime('%d-%m'):
                result.zodiac = zod_name

    # count age

    born = date_of_birth.date()
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    result.age = age

    return result


print(find_zodiac_sign())