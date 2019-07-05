# Model Writing Guidelines

Keep in mind the following things while creating new models.

1. Create one Model class in one file only.
2. Name of class will start from Capital letter and follow Camel Case.
3. Class Name should be Singular whereas the file name will be the plural form of the class name
4. If you use a custom Error Class, define it in ```errors.py``` and import it, same goes for enums.
5. If your model has many-to-many relationship with any other model, you need to define a junction table.
       For that, check the dbdiagram. Add the table in the file that contains the first class in the junction table's name.
6. If you are unsure that one db.relationship is defined in your model's target model or not, define the same in your model. Redundancy must be removed later.


# Testing

Always test the model locally and rollback changes in your local db after all tests are complete.
In no case, use the production database for testing.
Also do not hard-code username, password or db urls. Use environment variables for the same.

Current dbdiagram in use: <https://dbdiagram.io/d/5d1cdccfced98361d6dc4fde>
