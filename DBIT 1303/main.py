from .models import *
from .functions import *
from .database import *


#function to create a  new order
def create_order(meals):
    #getting the order number(random characters)
    order_number = get_order_number()
    # calculate the cost of the meal
    price = calculate_price(meals)
    #connection to sql 
    connection = connection("localhost", "admin", 12345, 'orders')
    add_order = """
        INSERT INTO orders VALUES
        (1,  ${order_number}, ${orders},${price},false,false),
        """ 
    perform_query(
        connection,
        add_order
    )
    return 'order created'
    
  #function to cancel an order  
def cancel_order(order):
    #retrieving the saved order
    connection = connection("localhost", "admin", 12345, 'orders')
    delete_order = """
        DELETE FROM orders WHERE
          order_number, ${orders.number};
        """ 
    #delete the order
    perform_query(
        connection,
        delete_order
    )
    return 'order cancelled'

#function to schedule order parts
def schedule_order_parts(order):
    #retrieve the order to be scheduled
    connection = connection("localhost", "admin", 12345, 'orders')
    #schedule parts of order
    update_order = """
        UPDATE orders  SET
          isScheduled = true WHERE order_number =${order.order_number};
        """
    add_meals = """
    INSERT INTO meals VALUES
    (1,  ${order.order_number}, ${order.order_meals[0]},${order.order_meals[0]}),
    """ 

    perform_query(
        connection,
       update_order
    ) 
    perform_query(
        connection,
       add_meals
    )
    #return scheduled order
    return 'order scheduled'

# function to pay for the order
def pay_for_order(order):
    connection = connection("localhost", "admin", 12345, 'orders')
    #update the order to pay for
    update_order = """
        UPDATE orders  SET
          isPaidFor = true WHERE order_number =${order.order_number};
        """ 
    #update payment
    perform_query(
        connection,
       update_order
    )
    #process payment of order and print receipt
    print_receipt(order)

    return 'Receipt printed'
