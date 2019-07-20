### MODELS

This directory gives all the DB models using SQLAlchemy's db.Model class. 
Current DB Diagram in use: https://dbdiagram.io/d/5d1cdccfced98361d6dc4fde

The structure is given as follows:
```` 
.
├── app
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── user.py
````
## Models Present:
**\_\_init\_\_:** Required by Python to mark the directory as a package directory.
**user:** DB Model for userdata such as username, email and Name.

# Creating A New Model
Update this file to reflect directory structure correctly and describe the contents of the created DB Table.
## Keep in mind the following things while creating new models.

* Create one Model class in one file only.  
* Name of class will start from Capital letter and follow Camel Case.  
* Class Name should be Singular whereas the file name will be the plural form of the class name
* If you use a custom Error Class, define it in errors.py and import it, same goes for enums.  
* If your model has many-to-many relationship with any other model, you need to define a junction table. For that, check the dbdiagram. Add the table in the file that contains the first class in the junction table's name.  
* If you are unsure that one db.relationship is defined in your model's target model or not, define the same in your model. Redundancy must be removed later.  
## Testing
Always test the model locally and rollback changes in your local db after all tests are complete.  In no case, use the production database for testing. Also do not hard-code username, password or  db urls. Use environment variables for the same.  

