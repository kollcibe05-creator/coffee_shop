# COFFEE_SHOP

`Coffee_shop` is literary a Domain model design of a Artcaffe  which implements OOP to betterfy its database management system.
The ideological business requirements are:

1. A Customer can place `many` Orders.
2. A Coffee can have `many` Orders.
3. An Order belongs to `one` Customer and `one` Coffee.

### Tech Stack
- Python
- Markdown


### File structure
It contains the following subdirectories:
**Class_files**: It contains the files *order.py* , *customer.py* and *coffee.py* which contain the classes with the corresponding names.

**testing**: It contains the files *test_order.py*, *test_coffee.py*, and *test_customer.py* which contain test cases for the corresponding classes.
It also contains the files:
``debug.py``: which provides interactive debugging while running the test cases.
``README.md``: contains the information you are reading now.

### Running the Tests
To runt the tests you need to set up a virtual environment within the directory;
```
pipenv install
pipenv shell 
```
Then run the tests;
```
pytest
```

or 
```
pytest -x
```
or 
```
pytest -s
```

### Functionality 
## 1. Customer.py 
 The Class `Customer` initializes with a `name`.
 It contains a setter and a getter to assert that the name is of instance str and has characters with len between 1 and 15.

 ##### oders(self) 
 Returns *Order* instances of the class `Order` for the customer.

 ##### coffees(self)
 Returns uniques instances of `coffee` instances for the *Order* class. 

 ##### create_order(self, coffee, price):
 Allows the customer to make an order but through the **Order** class to maintain the SSOT.

 ## 2. Coffee.py
Contains the `Coffee` Class that is initialized with a name `name `.
It also contains a setter and a getter to assert that the name parsed is a string of not less than three characters.

##### orders(self)
Returns  the *Order* instances of the coffee instance.

##### customers(self)
Returns unique instances of customers in the `Customer` class of the coffee instance.

##### num_orders(self)
It returns the number of times the coffee instance has been ordered by iterating through the `Order.all` list and adding the number of counts for every name instance that matches with the coffee instance.

##### average_price(self)
It returns the average of the total amount of money generated from the  coffee instance.
The list of the prices of the `coffee` instance in the **Order.all** list is generated after iteration.
It is then summed and divided by the numbers of orders calculated by the method ``self.num_orders(self)``.

##### most_afficionado  ~ *class method*
It returns the **name** of the best contributor of the parsed in coffee instance.
An empty dictionary is created to hold the name instance and the total number of contributions to the coffee instance parsed in.

The list of people extracted from `Order.all` is iterated and saved as a key in the empty dictionary and their instances as value.
``max()`` Python built-in function is used to extract the customer with the highest number of appearances in the dictionary.

## 3. Order.py ~ *SSOT*
It is the class instance that serves as the SSOT as it's work is to make the order and save all the orders in its list **Order.all**.
It contains setters and getter for;
- **Customer**: asserts that the customer parsed in is an instance of the `Customer` Class.

- **Coffee**: asserts that the coffee parsed in is an instance of the `Coffee` Class.

- **Price**: asserts that the price parsed in is an instance of the `Price` Class.



# Author
*Collins Kibet*

## [License](LICENSE)

MIT License
Copyright (c) 2025 Collins Kibet


# Contact info
* Email : kollcibe05@gmail.com










