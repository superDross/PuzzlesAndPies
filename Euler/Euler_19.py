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
def get_number_of_days(month, year):
    leap_years = [x for x in range(1904, 2001)][::4]
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

def get_sundays(weekday=2, sundays=0):
    for year in range(1901, 2001):
        for month in range(1, 13):
            days = get_number_of_days(month, year) + 1
            for day in range(1, days):
                if weekday == 7 and day == 1:
                    sundays += 1
                weekday = update_weekday(weekday)
    return sundays


# 171
answer = get_sundays()
print(answer)
