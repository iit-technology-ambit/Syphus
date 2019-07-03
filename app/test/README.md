### TEST


This directory contains Unit tests and other tests written using the Flask-Testing module.

**To run tests :** 
1. Change Directory to root folder of the app and run `pipenv shell`
2. Run `python manage.py test` or `make tests`. This will run all tests and display results. 

```` 
.
├── app
│   └── test
│       └── __init__.py
│       └── test_config.py

````

**test_config:** Contains 3 tests to test functionality in `Production`, `Developement` and `Testing` environments. 




