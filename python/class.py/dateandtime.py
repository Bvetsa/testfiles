import datetime

today = datetime.datetime.now()
year_now = today.year
month_now = today.month
week_now = today.strftime("%U")
weekday_now = today.strftime("%a")
day_year = today.strftime("%j")
day_month = today.strftime("%d")
day_week = today.strftime("%w")

def print_data():
    print(today)
    print(year_now)
    print(month_now)
    print(week_now)
    print(weekday_now)
    print(day_year)
    print(day_month)
    print(day_week)

def leap_year():
    year = (300)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                print(str(year) + " is a leap year")
            else:
                print(str(year) + " is not a leap year")
        else:
            print(str(year) + " is a leap year")
    else:
        print(str(year) + " is not a leap year")




dt_sample_date = datetime.datetime.strptime('Jan 1 2014 2:43PM', '%b %d %Y %I:%M%p')

now_time = datetime.datetime.now().time()
def date_tuday():
    from datetime import date, timedelta
    date_tday = date.today() - timedelta(5)
    print("Today is " + str(date.today()))
    print("5 days ago was " + str(date_tday))
    

print_data()
leap_year()
print(dt_sample_date)
print(now_time)
date_tuday()