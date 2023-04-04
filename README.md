# Validator - Python Data Validator


Python has all kinds of data validation tools, but every one of them seems to
require defining a schema or form. I wanted to create a simple validation
library where validating a simple value does not require defining a form or a
schema.

```python pip install Validator
>>> from validate import Validator


>>> data = {
    "user": {
        "name": {
            "first": "John",
            "last": "Doe"
        },
        "contact": {
            "email": "johndoe@example.com",
            "phone": {
                "home": "555-1234",
                "work": "555-5678"
            }
        },
        "address": {
            "street": 12312313,
            "city": "Anytown",
            "state": "CA",
            "zip": 12345,
            "coordinates": {
                "latitude": 37.7749,
                "longitude": -122.4194
            }
        }
    }
}

>>> rules = {
    "user.name.first": "required|string",
    "user.name.last": "required|string",
    "user.contact.email": "required|email",
    "user.contact.phone.home": "string",
    "user.contact.phone.work": "string",
    "user.address.street": "required|string",
    "user.address.city": "required|string",
    "user.address.state": "required|string",
    "user.address.zip": "required|integer",
    "user.address.coordinates.latitude": "required|float",
    "user.address.coordinates.longitude": "required|float"
}

>>> validator = Validator(data, rules)
>>> errors = validator.validate()
>>> if errors:
    >>> print(errors)
