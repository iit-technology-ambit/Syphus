# Common Backend for Ambit

This is the common backend for Tech-Ambit web and android application.

# Directory structure
```` 
    .
    |──rest_apis/
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

Collect all similar endpoints in 1 file in `endpoints` folder. Use different files for logically dissimilar endpoints.

# Setting up the project locally
Please use pipenv. To install pipenv
Run `pip install pipenv`

Please use a separate virtual environment by running ` pipenv shell ` and then run `pipenv install` to install all dependencies.

# Installing new dependencies
To install a new dependency, use `pipenv install <pkg-name> `. 
This will update Pipfile and Pipfile.lock

To upgrade a package, use ` pipenv update <pkg-name> `.

# Adding new dependencies to requirements.txt

Whenever a new dependency is used, be sure to run 
````
pip freeze > requirements.txt
````
Mention dependency change in the commit message.
