#class for an orde object
class Order:
  def __init__(self, order_number, ordered_meals,order_price,isScheduled,isPaidFor):
    self.order_number = order_number
    self.ordered_meals = ordered_meals
    self.order_price = order_price
    self.isScheduled = isScheduled
    self.isPaidFor = isPaidFor

# class for meals that is the starter and main course
class Meals:
  def __init__(self,order_number, starter, main_course):
    self.order_number
    self.order_number = order_number
    self.ordered_meals = ordered_meals
    self.meal_price = meal_price

    
class Receipt:
    def __init__(self,order_number, amount,date):
      self.order_number
      self.amount
      self.date