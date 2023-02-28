from cerberus import Validator


class ValidateProviders:
    """
    {
    "name": "bank_name",
    }
    Fields:
        name_provider: str, maxlength: 255 | Required
        nit_provider: str, maxlength: 11 | Required
        name_contact_person, maxlength: 255 | Required
        bank: instance Relations Banks Models | Required
        number_contact_person: str, maxlength: 10 | None
        number_account_banking: str,  maxlength: 15 | None

    Validations:
    allowed in Cerberus is the main validations, See: https://docs.python-cerberus.org/en/stable/validation-rules.html#allowed
    But in this case i need to says at the user's which one in the list available

    This Works! but i won't use it
    "bank": {
        "type": "string",
        "required": True,
        "maxlength": 50,
        "allowed": list(Banks.objects.filter(is_active=True).values_list("name_bank", flat=True))
    }
    """

    schema = {
        "name_provider": {
            "type": "string",
            "required": True,
            "maxlength": 255,
        },
        "nit_provider": {
            "type": "string",
            "required": True,
            "maxlength": 11,
        },
        "name_contact_person": {
            "type": "string",
            "required": True,
            "maxlength": 255,
        },
        "number_contact_person": {
            "type": "string",
            "required": False,
            "maxlength": 10,
        },
        "number_account_banking": {
            "type": "string",
            "required": False,
            "maxlength": 15,
        },
        "bank": {
            "type": "string",
            "required": True,
            "maxlength": 50,
        },
    }

    def __init__(self, data):
        self.validator = Validator()
        self.data = data
        self.schema = self.__class__.schema

    def validate(self):
        return self.validator.validate(self.data, self.schema)

    def errors(self):
        return self.validator.errors
