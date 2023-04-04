class Validator:
    def __init__(self, data, rules):
        self.data = data
        self.rules = rules
    
    def validate(self):
        errors = {}
        for field, rule in self.rules.items():
            value = self.get_value(field, self.data)
            checks = rule.split("|")
            for check in checks:
                if not hasattr(self, check):
                    raise ValueError(f"Invalid validation rule: {check}")
                method = getattr(self, check)
                if not method(value):
                    errors[field] = f"Invalid value for '{field}'."
        return errors if errors else None
    
    def get_value(self, field, data):
        if '.' not in field:
            return data.get(field)
        else:
            fields = field.split('.')
            value = data.get(fields[0])
            for f in fields[1:]:
                if isinstance(value, dict):
                    value = value.get(f)
                else:
                    return None
            return value
    
    def required(self, value):
        return value is not None and value != ""
    
    def string(self, value):
        return isinstance(value, str)
    
    def integer(self, value):
        return isinstance(value, int)
    
    def float(self, value):
        return isinstance(value, float)
    
    def email(self, value):
        import re
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        return re.match(email_regex, value)
    
    def array(self, value):
        return isinstance(value, list)
    
    def boolean(self, value):
        return isinstance(value, bool)

data = {
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

rules = {
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

validator = Validator(data, rules)
errors = validator.validate()
if errors:
    print(errors)
