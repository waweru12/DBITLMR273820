import random
import string
from .models import *
import datetime

def get_order_number():
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(3))
    result_num = str(random.randint(1000,9999))  
    return result_str+result_num


def print_receipt(order):
    receipt = Receipt(
        order_number=order.order_number,
        amount=order.price,
        date=datetime.now()
    )
    print('receipt printed')
    return receipt

def calculate_price(meals):
    price = 0
    for i in meals:
        meal = """
        SELECT * FROM meals WHERE
          meal_name, ${meal};
        """ 
        price += meal.meal_price
    return price