import pytest
import sys 
import os 

current_dir = os.path.dirname(__file__)
parent_directory = os.path.join(current_dir, "..")
sys.path.insert(0, parent_directory)

from coffee import Coffee, Order, Customer
# cappuccino = Coffee("cappuccino")
# espresso = Coffee("espresso")
# mochas = Coffee("mochas")
#    
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


class TestCoffee:
    """Tests For Coffee Class"""

    def test_has_name(self):
        """Coffee is initialized with a name"""
        cappuccino = Coffee("cappuccino")
        assert cappuccino.name == "cappuccino"
    pass    

    def test_name_has_valid_number_of_characters(self):
        """Name is a string with characters not less than 3"""
        cappuccino = Coffee("cappuccino")
        assert len(cappuccino.name)>=3

        short_name = ""    
        with pytest.raises(ValueError):
            Coffee(short_name)

class TestCustomer:
    """Tests for the Customer Class"""  
    def test_has_name(self):
        """Customer is intitialized with a name"""
        nekesa = Customer("Nekesa")

        assert nekesa.name == "Nekesa"
    def test_name_validity_and_length(self):
        """Name is a string with characters between 1 and 15"""
        nekesa = Customer("Nekesa")
        assert isinstance(nekesa.name, str) and 1<len(nekesa.name)<15

        with pytest.raises(ValueError):
            Customer(15)



class TestOrder:
    """Tests for Order Class"""
    def test_init_values(self):
        '''Order initializes with customer, coffee and price''' 
        cappuccino = Coffee("cappuccino")
        espresso = Coffee("espresso")
        mochas = Coffee("mochas")
   
        wafula = Customer("Wafula") 
        nekesa = Customer("Nekesa")
        kotlin = Customer("Kotlin")
        onika = Customer("Onika")                                                                                                  # print(wafula.name)

        order_1 = Order(wafula, cappuccino, 9.1)
        order_2 = Order(wafula, cappuccino, 9.1)
        order_3 = Order(nekesa, cappuccino, 9.9)
        order_4 = Order(wafula, cappuccino, 9.1)

        order_5 = nekesa.create_order(espresso, 6.9) 
        order_6 = kotlin.create_order(espresso, 6.9)

        order_7 = Order(onika, mochas, 9.1)
 

        assert order_1.customer  == wafula 
        assert order_1.coffee == cappuccino
        assert order_1.price == 9.1

    def test_customer_class_instance(self):
        """Customer is an instance of the Customer Class"""
        cappuccino = Coffee("cappuccino")
        espresso = Coffee("espresso")
        mochas = Coffee("mochas")
   
        wafula = Customer("Wafula") 
        nekesa = Customer("Nekesa")
        kotlin = Customer("Kotlin")
        onika = Customer("Onika")                                                                                                  # print(wafula.name)

        order_1 = Order(wafula, cappuccino, 9.1)
        order_2 = Order(wafula, cappuccino, 9.1)
        order_3 = Order(nekesa, cappuccino, 9.9)
        order_4 = Order(wafula, cappuccino, 9.1)

        order_5 = nekesa.create_order(espresso, 6.9) 
        order_6 = kotlin.create_order(espresso, 6.9)

        order_7 = Order(onika, mochas, 9.1)
        assert isinstance(order_1.customer, Customer)

        with pytest.raises(TypeError):
            Order("Collo", cappuccino, 8.6)


    def test_coffee_class_instance(self):
        cappuccino = Coffee("cappuccino")
        espresso = Coffee("espresso")
        mochas = Coffee("mochas")
   
        wafula = Customer("Wafula") 
        nekesa = Customer("Nekesa")
        kotlin = Customer("Kotlin")
        onika = Customer("Onika")                                                                                                  # print(wafula.name)

        order_1 = Order(wafula, cappuccino, 9.1)
        order_2 = Order(wafula, cappuccino, 9.1)
        order_3 = Order(nekesa, cappuccino, 9.9)
        order_4 = Order(wafula, cappuccino, 9.1)

        order_5 = nekesa.create_order(espresso, 6.9) 
        order_6 = kotlin.create_order(espresso, 6.9)

        order_7 = Order(onika, mochas, 9.1)
        assert isinstance(order_1.coffee, Coffee)

        with pytest.raises(TypeError):
            Order(wafula, "Americanos", 7.5)

    def test_price_validity(self):
        cappuccino = Coffee("cappuccino")
        espresso = Coffee("espresso")
        mochas = Coffee("mochas")
   
        wafula = Customer("Wafula") 
        nekesa = Customer("Nekesa")
        kotlin = Customer("Kotlin")
        onika = Customer("Onika")                                                                                                  # print(wafula.name)

        order_1 = Order(wafula, cappuccino, 9.1)
        order_2 = Order(wafula, cappuccino, 9.1)
        order_3 = Order(nekesa, cappuccino, 9.9)
        order_4 = Order(wafula, cappuccino, 9.1)

        order_5 = nekesa.create_order(espresso, 6.9) 
        order_6 = kotlin.create_order(espresso, 6.9)

        order_7 = Order(onika, mochas, 9.1)
        
        assert isinstance(order_1.price, float) and 1.0<(order_1.price)<10.0

        with pytest.raises(TypeError):
            Order(wafula, cappuccino, 10.1) 
    

                





            
            



        
