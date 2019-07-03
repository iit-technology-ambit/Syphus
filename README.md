# Common Backend for Ambit

This is the common backend for Tech-Ambit web and android application.

# Directory structure
```` 
.
├── app
│   ├── __init__.py
│   ├── main
│   │   ├── config.py
│   │   ├── controller
│   │   │   ├── auth_controller.py
│   │   │   ├── __init__.py
│   │   │   └── user_controller.py
│   │   ├── __init__.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   ├── service
│   │   │   ├── auth_helper.py
│   │   │   ├── __init__.py
│   │   │   └── user_service.py
│   │   └── util
│   │       └── __init__.py
│   └── test
│       └── __init__.py
├── manage.py
├── Makefile
├── Pipfile
├── Pipfile.lock
├── README.md
└── requirements.txt

````

This can improved though.

Collect all similar endpoints in the `app/controller` folder. Use different files for logically dissimilar endpoints.

# Setting up the project locally
Please use pipenv. To install pipenv
Run `pip install pipenv`

Please use a separate virtual environment by running ` pipenv shell ` and then run `pipenv install` to install all dependencies.
to install all dependencies.

# Adding new dependencies

To install a new dependency, use `pipenv install <pkg-name> `. 
This will update Pipfile and Pipfile.lock

To upgrade a package, use ` pipenv update <pkg-name> `.

Whenever a new dependency is used, be sure to run 
````
pip freeze > requirements.txt
````
Mention dependency change in the commit message.

# Using Makefile

## Initial installation

```
make install
```

## To run tests
```
make tests
```

## Run application
```
make run
```

## Run all commands at once
```
make all
```

# Docker Container

To build the container, make sure that the Dockerfile is present and run `docker build -t common-backend:latest .` 

To run the application from the docker container, run `docker run common-backend ARG` where `ARG` can be `db`, `run, test`, `shell` or `runserver`.  
For more information, run `docker run common-backend --help`.