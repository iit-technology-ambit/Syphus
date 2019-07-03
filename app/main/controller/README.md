## CONTROLLER

This directory contains all API endpoints, which handle incoming HTTP requests. Place all logically dissimilar endpoints in different files, such as login/logout and user operation API's.

### Directory structure
```` 
.
├── app
│   ├── __init__.py
│   ├── main
│   │   ├── controller
│   │   │   ├── auth_controller.py
│   │   │   ├── __init__.py
│   │   │   └── user_controller.py

````

### API's Present
 **user_controller:** Contains API Endpoints related to user operations, such as getting a list of all users and finding if a user is present or not. 
 
 **auth_controller:** Contains API Endpoints related to login/logout operations. Creates endpoint to Add and Remove users. 
 
 ### Creating A New Endpoint
 
Update this file to reflect directory structure correctly and describe the contents of the created endpoints in this file.