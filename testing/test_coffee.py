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
    def test_num_orders_method(self):  
        """num_orders(self) returns the number of orders the coffee has"""      
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

        assert cappuccino.num_orders() == 4
        assert espresso.num_orders() == 2

    def test_average_price_method(self):
        """average_price(method) returns the average amount of money spent on the coffee instance"""
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

        assert cappuccino.average_price() == 9.3
        assert espresso.average_price() == 6.9

    def test_most_afficionado(self):
        """most_afficionado(cls, coffee) a class method that returns the best  buyer of the passed in coffe name"""
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

        assert Coffee.most_afficionado(cappuccino) == "Wafula"
        assert Coffee.most_afficionado(mochas) == "Onika"

        americanos = Coffee("Americano")
        assert Coffee.most_afficionado(americanos) == None
            
