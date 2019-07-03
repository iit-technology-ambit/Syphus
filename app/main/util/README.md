## UTIL

This directory contains utilities required for the application to transfer data and responses between API Endpoints. 

### Directory structure
```` 
.
├── app
│   ├── main
│   │   └── util
│   │       └── __init__.py
			└── dto.py
			└── authentication.py

````

### Utilities Present

**dto:** The data transfer object (DTO) will be responsible for carrying data between processes. In our case, this is used to convert the login input data to api.model class object. 

**authentication** Contains decorators to determine if the user is logged in and if the user is an admin. Returns a response object based on the logged in state. 