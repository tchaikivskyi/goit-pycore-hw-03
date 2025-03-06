from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    if not isinstance(users, list): 
        raise TypeError('The users must be a list.')
    
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days
        if 0 <= delta_days <= 7:
            if birthday_this_year.weekday() in [5, 6]:  
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays


users = [
    {"name": "John Doe 1", "birthday": "1985.03.04"},
    {"name": "John Doe 2", "birthday": "1985.03.09"},
    {"name": "John Doe 3", "birthday": "1990.03.12"},
    {"name": "John Doe 4", "birthday": "1990.03.14"},
    {"name": "John Doe 5", "birthday": "2000.03.16"},
    {"name": "John Doe 6", "birthday": "1995.03.17"},
]

print(get_upcoming_birthdays(users))
