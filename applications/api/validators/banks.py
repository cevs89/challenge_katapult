from cerberus import Validator


class ValidateBanks:
    """
    {
    "name": "bank_name",
    }
    """

    schema = {
        "name": {
            "type": "string",
            "required": True,
            "maxlength": 50,
        }
    }

    def __init__(self, data):
        self.validator = Validator()
        self.data = data
        self.schema = self.__class__.schema

    def validate(self):
        return self.validator.validate(self.data, self.schema)

    def errors(self):
        return self.validator.errors
