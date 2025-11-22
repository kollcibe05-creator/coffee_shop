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



class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    # coffe_name property
    @property
    def name(self):
        return self._name
    @name.setter    
    def name(self, name):  
        if isinstance(name, str) and len(name)>=3:
            self._name = name    
        else:
            raise ValueError("name must be a string with at least 3 characters")  
    
    def orders(self):
        return [order for order in Order.all  if order.coffee is self]

    def customers(self):
        return list(set([order.customer for order in self.orders()]))      #Order.all if order.coffee is self


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
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of the Customer Class") 
        self._customer = customer        


    #setting coffee_ property
    @property
    def coffee(self):
        return self._coffee 
    @coffee.setter
    def coffee(self, coffee):
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






# cappuccino = Coffee("cappuccino")
# print(cappuccino.name)

# wafula = Customer("Wafula") 
# print(wafula.name)


# order_1 = Order(wafula, cappuccino, 9.1)
# print(order_1.price)
# print(order_1._coffee)
# print(order_1._customer)

# print(order_1.customer.name)

# print(list(set([1,4,6,4,7,2])))