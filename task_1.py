from datetime import datetime as dt

def get_days_from_today(date: str) -> int:
    if not isinstance(date, str): 
        raise TypeError('The date must be a string in the format "YYYY-MM-DD".')
    
    try:
        date_now = dt.today()
        date_from_user = dt.strptime(date, '%Y-%m-%d')
        count_days_from_date = date_now - date_from_user
        return count_days_from_date.days
    except ValueError:
        raise ValueError('Invalid date format. Please use "YYYY-MM-DD".')
        


print(get_days_from_today('2020-10-09'))
print(get_days_from_today('2026-07-01'))
# print(get_days_from_today(2))
# print(get_days_from_today(None))