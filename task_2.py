import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if not isinstance(min, int) and not isinstance(max, int) and not isinstance(quantity, int): 
        raise TypeError('The values "min, max, quantity" must be a int.')
    
    if min < 1:
        raise 'Min value must be more than 1.' 
    elif max > 1000:
        raise 'Max value must be less than 1000.' 
    elif quantity > (max - min + 1):
        raise 'Quantity value must be less or equal than range of numbers.' 
        
    range_numbers = random.sample(range(min, max + 1), quantity)
    
    return sorted(range_numbers)
        


print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 36, 5))
# print(get_numbers_ticket(-1, 36, 5))
# print(get_numbers_ticket(1, 1001, 5))
# print(get_numbers_ticket(5, 8, 5))

