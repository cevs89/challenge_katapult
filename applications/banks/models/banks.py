from django.core.exceptions import ValidationError
from django.db import models

from applications.core.models import BaseModel
from applications.utils.functions import normalize_frase


class Banks(BaseModel):
    """
    This models represent all banks list.
        Field Required:
            name_bank: str -> max_length 50
        Fiels heritage - BaseModel
            uuid
            is_active
            created_at
            modified_at
    """

    name_bank = models.CharField(max_length=50, null=False, unique=True)

    def save(self, *args, **kwargs):
        """
        Nomalize lower string into the name
        """
        try:
            self.name_bank = normalize_frase(self.name_bank)
        except Exception as e:
            raise ValidationError(str(e))

        return super(Banks, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"

    def __str__(self):
        return self.name_bank
