# from typing import TYPE_CHECKING
from .order import Order

# if TYPE_CHECKING:
#    from .order import Order

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
    #name property
    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if  isinstance(name, str) and   1< len(name) <15:
            self._name = name  
        else:
            raise ValueError("Name must be an integer with  between 1 and 15 characters")

    def orders(self):
        return [order for order in Order.all if order.customer is self]
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))       #Order.all if order.customer is self
    def create_order(self, coffee, price):
        Order(self, coffee, price) 
