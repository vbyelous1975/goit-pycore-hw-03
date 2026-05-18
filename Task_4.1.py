from datetime import datetime


def get_days_from_today(date: str) -> int:
    try:
        datetime_object = datetime.strptime(date, "%Y-%m-%d")
    except ValueError, TypeError:
        return None
    current_date = datetime.today()
    difference = datetime_object - current_date
    return difference.days

date = "20201-10-09"
result = get_days_from_today(date)
print(result)

string_date = 22222
result = get_days_from_today(string_date)
print(result)

result = get_days_from_today("2020-10-09")
print(result)
