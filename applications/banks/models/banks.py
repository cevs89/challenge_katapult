from django.db import models

from applications.core.models import BaseModel


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

    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"

    def __str__(self):
        return self.name_bank
