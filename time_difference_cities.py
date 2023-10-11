import pytz
from pytz import timezone
from datetime import datetime

def time_between_city(city1, city2):

    city1tz = ''
    city2tz = ''

    server_time = datetime.now()

    #city 1 section

    for tz in pytz.all_timezones:
        if city1.capitalize() in tz:
            city1tz = tz
            print(city1tz)
            city1time = timezone(city1tz).fromutc(server_time)
        else:
            continue

    if city1tz == '':
        print("No such city 1 in the DB")

    print(city1time.strftime('%X'))

    # city 2 section

    for tz in pytz.all_timezones:
        if city2.capitalize() in tz:
            city2tz = tz
            print(city2tz)
            city2time = timezone(city2tz).fromutc(server_time)
        else:
            continue

    if city2tz == '':
        print("No such city 1 in the DB")

    print(city2time.strftime('%X'))

    # Difference section

    format = "%z"

    holder1 = city1time.strftime(format)
    diff1 = float(holder1)
    print(diff1)
    print(timezone(city1tz).fromutc(server_time))

    holder2 = city2time.strftime(format)
    diff2 = float(holder2)
    print(diff2)
    print(timezone(city2tz).fromutc(server_time))

    if diff1 >= 0 and diff2 >= 0:
        diff = abs(diff1 - diff2)
    elif diff1 <= 0 and diff2 <= 0:
        diff = abs(diff1 - diff2)
    elif diff1 <= 0 and diff2 >= 0:
        diff = diff2 - diff1
    elif diff2 <= 0 and diff1 >= 0:
        diff = abs(diff1 - diff2)

    diff = str(int(diff))

    if diff1 % 100 != 0 or diff2 % 100 !=0:
        diff = diff[:1] + '.5'
    elif int(diff) > 1000:
        diff = diff[:2]
    elif int(diff) < 1000:
        diff = diff[:1]

    if holder1 == holder2:
        print('There is no time difference between cities.')
    elif diff1 < diff2:
        print('The ' + city1.capitalize() + ' is ' + diff + ' hours ahead of ' + city2.capitalize())
    elif diff2 < diff1:
        print('The ' + city2.capitalize() + ' is ' + diff + ' hours ahead of ' + city1.capitalize())

time_between_city('Marquesas', 'Zulu')