''' Euler 19

You are given the following information, but you may prefer to do some research for yourself.

    - 1 Jan 1900 was a Monday.
    - Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    - A leap year occurs on any year evenly divisible by 4, 
      but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
import numpy as np

NUM2DAY = {1: 'Monday', 2: 'Tuesday', 3: 'Wednseday', 4: 'Thursday', 
           5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

def get_number_of_days(month, year):
    leap_years = np.arange(1904, 2018)[::4]
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and year in leap_years:
        return 29
    elif month == 2 and year not in leap_years:
        return 28
    else:
        return 31

def update_weekday(weekday):
    weekday += 1
    if weekday > 7:
        weekday = 1
    return weekday

def get_weekday(date):
    date = [int(x) for x in date.split("/")]
    weekday = 0
    for year in range(1900, 2018):
        for month in range(1, 13):
            days = get_number_of_days(month, year) + 1
            for day in range(1, days):
                weekday = update_weekday(weekday)
                if [day, month, year] == date: 
                    return (NUM2DAY[weekday], day, month, year)


# Sunday
answer = get_weekday('31/12/2000')
print(answer)
