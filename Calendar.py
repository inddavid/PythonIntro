import calendar

def show_calendar(year):
    for month in range(1, 13):
        print(calendar.month(year, month))

show_calendar(2026)

