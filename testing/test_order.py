
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
        """Coffee is an instance of the Coffee Class"""
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
        """Price is a float of value between 1.0 and 10.0"""
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


                





            
            



        
