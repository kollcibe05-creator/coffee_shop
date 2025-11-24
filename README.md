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

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**testing**: It contains the files *test_order.py*, *test_coffee.py*, and *test_customer.py* which contain test cases for the corresponding classes.
It also contains the files:
``debug.py``: which provides interactive debugging while running the test cases.
``README.md``: contains the information you are reading now.

### Running the Tests
To set up the virtual environment you need to set up a virtual environment within the directory;
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

```testing sth ```
""moew""



