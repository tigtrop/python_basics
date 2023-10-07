import datetime
from datetime import timedelta


def find_friday13(howmuch):

    today = datetime.date.today()
    iterator = 0

    for single_date in (today + timedelta(n) for n in range(5000*howmuch)):
        if iterator < howmuch:
            if '13' in str(single_date) and single_date.strftime('%A') == 'Friday':
                print(single_date)
                iterator += 1
        else:
            break


find_friday13(10)
