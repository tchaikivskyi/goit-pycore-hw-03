import re

def normalize_phone(phone_number: str) -> str:
    if not isinstance(phone_number, str): 
        raise TypeError('The phone number must be a string in the format "+380000000000".')
    
    formated_number = re.sub(r'[^\d+]', '', phone_number.strip())

    if formated_number.startswith('380'):
        return f'+{formated_number}'
    
    if formated_number.startswith('+'):
        return formated_number
    
    return f'+38{formated_number}'


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
# print(normalize_phone(123))
# print(normalize_phone(None))