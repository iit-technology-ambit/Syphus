## SERVICE

This directory contains all business logic related to the application, such as handling all the logic related to user information. 

### Directory structure
```` 
.
├── app
│   ├── __init__.py
│   ├── main
│   │   ├── service
│   │   │   ├── auth_helper.py
│   │   │   ├── __init__.py
│   │   │   └── user_service.py

````

### Classes Present

**user_service:** This class handles all the logic related to the user model. This class imports the user model defined in the app.models.user class. This also provides a template to create a new user and commit changes to the database. 

**auth_service:** This contains a helper class for all authentication related operations such as checking user/password with the database and returning a response object for authentication processes. 

 ### Creating A New Endpoint
 
Update this file to reflect directory structure correctly and describe the contents of the created helper classes in this file.
