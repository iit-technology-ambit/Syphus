# Contributing

The document contains general guidelines regarding contributing ethics to the project.

## Installation and Setup

To setup the project, refer [here](https://github.com/iit-technology-ambit/common-backend/blob/master/README.md)

The first and foremost action to do after set up is to install using `pre-commit install`. This will install all the pre-commit sanitation hooks and ensure that your code
is top notch.

## Etiquettes

We follow certain etiquettes which are as follows:

- Every code has a right place and right function (create if it doesn't exist) where it belongs.
- Each function must have docstring of the below format.

```python
"""
[summary]

[long description if required]

:param arg: [description]
:type arg: [type]
:return: [description]
:rtype: [type]
"""
```

- Each module and class must have a single line docstring.
- New folders should have a README.md mentioning what belongs there.
- Pull Requests must have good description with appropriate attachments such as screenshots.

## Tests

The project is tested via Travis CI. The following tests are performed automatically:

- mypy: For type checking
- pylama: For code auditing
- isort: For sorting the imports automatically
- python unittests

## DocStrings Testing

All the docstrings are tested for the above mentioned guidelines via `pydocstyle`.

### Thank you.

You are an important part of this project, please maintain respect towards other developers, give polite reviews on Pull requests, and don't forget to live life.
