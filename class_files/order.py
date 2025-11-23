# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from .coffee import Coffee
#     from .customer import Customer



class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    #setting customer to be of class Customer
    @property  
    def customer(self):
        return self._customer  
    @customer.setter
    def customer(self, customer):
        from .customer import Customer
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of the Customer Class") 
        self._customer = customer        


    #setting coffee_ property
    @property
    def coffee(self):
        
        return self._coffee 
    @coffee.setter
    def coffee(self, coffee):        
        from .coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of the Coffee Class")  
        self._coffee = coffee  

    #price property
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0 <price<10.0:
            self._price = price
        else:
            raise TypeError("Price must be a float between 1.0 and 10.0")    
