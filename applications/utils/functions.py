import re
from unicodedata import normalize

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def normalize_frase(_text):
    _nomalize_text = normalize("NFC", _text)
    return _nomalize_text.lower().strip()


def validate_nit(value):
    """
    Validate 9 digiti before de dash.
    If it has a dash i'll go to validate, but if it doesn't, just will accept 9 digit
    """
    _nit = value.split("-")
    if not len(_nit[0]) == 9:
        raise ValidationError(
            _("%(value)s must be 9 digit before the dash (-) or just 9 digit"),
            params={"value": value},
        )

    """
    Validate if has the dash after the last digit, it's doesn't has we don't
    validate de pattern, because the last number it's options.

    Spanish Requirement:
        NIT del proveedor debe ser tipo string y seguir la estructura 9 dígitos un guión
        medio (-) y un dígito opcional.
    """
    if "-" in value and not re.search(r"^(^[0-9]+-{1}[0-9]{1})", value):
        raise ValidationError(
            _("%(value)s isn't a valid NIT"),
            params={"value": value},
        )
