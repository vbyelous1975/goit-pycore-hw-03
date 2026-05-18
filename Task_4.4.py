from datetime import datetime, timedelta



def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        print(birthday_this_year)
        if birthday_this_year >= today and birthday_this_year <= (today + timedelta(days=7)):
            checking_weekday = birthday_this_year.weekday()
            if checking_weekday == 5:  # Saturday
                birthday_this_year = birthday_this_year + timedelta(days=2)
                
            elif checking_weekday == 6:  # Sunday
                birthday_this_year = birthday_this_year + timedelta(days=1)
                
            else:
                birthday_this_year = birthday_this_year
            upcoming_birthdays.append({'name': user['name'],'congratulation_date': str(birthday_this_year)})
    return upcoming_birthdays



users = [{"name": "John Dog", "birthday": "1985.05.15"}, {"name": "Silvia Cat", "birthday": "1988.05.17"}, {"name": "Michael Mouse", "birthday": "1990.05.20"}, {"name": "Emily Rabbit", "birthday": "1992.05.22"}, {"name": "David Fox", "birthday": "1987.05.31"}]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
