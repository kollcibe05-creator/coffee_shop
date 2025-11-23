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
    
    ###must be tested####
    def num_orders(self):
        count = 0
        for order in Order.all:
            if order.coffee is self:     ##len of self.orders() ~ didn't work 
                count += 1
        return count  
        # all_orders = len(self.orders())
        # all_orders = len([orders for orders in self.orders()])
        # print(all_orders)

    def average_price(self):
        sum_of_prices_for_the_coffee = sum([order.price for order in Order.all if order.coffee is self])
        avg = sum_of_prices_for_the_coffee/ self.num_orders()
        return avg
        # num_of_orders = [num for num in num_orders()]
        # summation = sum(prices_for_the_coffee)
        # avg = summation/num_orders()
        # return avg

    @classmethod    
    def most_afficionado(cls, coffee):
        dict_holder = {}
        people_ordered =  [order.customer for order in Order.all if order.coffee is coffee]
        dict_holder = {}
        if people_ordered != []:
            for person in people_ordered:            
                dict_holder[person.name] = dict_holder.get(person.name, 0) + 1
            best_contributor = (max(dict_holder, key= lambda x: x))
            return best_contributor if best_contributor else None
            # return ("The most contributed times:", max(dict_holder.values()))
            # print(people_ordered)
            # print(max(dict_holder, key =lambda item: item[1] ))      # else None 
        else:
             return None    





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






cappuccino = Coffee("cappuccino")
espresso = Coffee("espresso")
mochas = Coffee("mochas")
                                                                                            # print(cappuccino.name)

wafula = Customer("Wafula") 
nekesa = Customer("Nekesa")
kotlin = Customer("Kotlin")
onika = Customer("Onika")
                                                                                            # print(wafula.name)


order_1 = Order(wafula, cappuccino, 9.1)
order_2 = Order(wafula, cappuccino, 9.1)
order_3 = Order(nekesa, cappuccino, 9.9)
order_4 = Order(wafula, cappuccino, 9.1)

order_5 = nekesa.create_order(espresso, 6.9) 
order_6 = kotlin.create_order(espresso, 6.9)


order_7 = Order(onika, mochas, 9.1)


# for order in wafula.orders():
#     print(order.coffee.name)
   
# print(wafula.orders())

# for order in nekesa.orders():
#     print(order.coffee.name)
   
# print(nekesa.orders())

# print(onika.coffees())
# print(nekesa.coffees())



# print(order_1.price)
# print(order_1._coffee)
# print(order_1._customer)

# print(order_1.customer.name)

# print(list(set([1,4,6,4,7,2])))

# print(cappuccino.orders())
# print(espresso.orders())


# print(mochas.customers())




# print(Coffee.most_afficionado(espresso))

# print(cappuccino.num_orders())

# print(cappuccino.average_price())


# dict_example = {"Collo": "99", "Mellow":"98"}
# print(max(list(dict_example), key= lambda x: x[1]))

# print(Coffee.most_afficionado(cappuccino))

# print(order_1.customer == wafula)

# print(wafula.coffees())

# print(order_5 in Order.all)