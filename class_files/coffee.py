# from typing import TYPE_CHECKING
from .order import Order

# if TYPE_CHECKING:
#     from .order import Order

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










# cappuccino = Coffee("cappuccino")
# espresso = Coffee("espresso")
# mochas = Coffee("mochas")
#                                                                                             # print(cappuccino.name)

# wafula = Customer("Wafula") 
# nekesa = Customer("Nekesa")
# kotlin = Customer("Kotlin")
# onika = Customer("Onika")
#                                                                                             # print(wafula.name)


# order_1 = Order(wafula, cappuccino, 9.1)
# order_2 = Order(wafula, cappuccino, 9.1)
# order_3 = Order(nekesa, cappuccino, 9.9)
# order_4 = Order(wafula, cappuccino, 9.1)

# order_5 = nekesa.create_order(espresso, 6.9) 
# order_6 = kotlin.create_order(espresso, 6.9)


# order_7 = Order(onika, mochas, 9.1)


# # for order in wafula.orders():
# #     print(order.coffee.name)
   
# # print(wafula.orders())

# # for order in nekesa.orders():
# #     print(order.coffee.name)
   
# # print(nekesa.orders())

# # print(onika.coffees())
# # print(nekesa.coffees())



# # print(order_1.price)
# # print(order_1._coffee)
# # print(order_1._customer)

# # print(order_1.customer.name)

# # print(list(set([1,4,6,4,7,2])))

# # print(cappuccino.orders())
# # print(espresso.orders())


# # print(mochas.customers())




# # print(Coffee.most_afficionado(espresso))

# # print(cappuccino.num_orders())

# # print(cappuccino.average_price())
# # print(espresso.average_price())


# # dict_example = {"Collo": "99", "Mellow":"98"}
# # print(max(list(dict_example), key= lambda x: x[1]))

# # print(Coffee.most_afficionado(cappuccino))

# # print(order_1.customer == wafula)

# # print(wafula.coffees())

# # print(order_5 in Order.all)

# # print(Coffee.most_afficionado(espresso))