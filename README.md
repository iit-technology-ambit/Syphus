# Flask Backend for Ambit
==============================
This is the repo for REST apis to be used.
We will be using **Flask** with **SQLAlchemy** and **flask_restplus**

# Directory structure
```` 
    .
    ├──rest_apis/
    |    ├── database
    |    │   ├── __init__.py
    |    │   └── models.py
    |    ├── endpoints
    |    │   └── __init__.py
    |    ├── __init__.py
    |    ├── settings.py
    |    ├── static/
    |    └── templates/
    |
    ├──tests/
    |
    ├──README.md
    |
    ├──requirements.txt
````

This can improved though.

Collect all similar endpoints in 1 file in ````endpoints```` folder. Use different files for logically dissimilar endpoints.

# Setting up the project locally
Please use a separate virtual environment. If you use a name other than ````venv````, do add that in ````.gitignore````
Run 
````
pip install requirements.txt
```` 
to install all dependencies.

# Adding new dependencies
Whenever a new dependency is used, be sure to run 
````
pip freeze > requirements.txt
````
Mention dependency change in the commit message.