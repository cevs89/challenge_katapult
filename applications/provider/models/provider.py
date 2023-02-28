from django.db import models

from applications.utils.functions import validate_nit
from applications.utils.models import BaseModel


class Provider(BaseModel):
    """
    This models represent all banks list.
        Field Required:
            name_provider: str -> max_length 255 | Required
            nit_provider: str -> max_length 9 | Required
            name_contact_person: str -> max_length 255 | Required
            number_contact_person: str -> max_length 10 | None
            number_account_banking: str -> max_length 15 | None
        Fiels heritage - BaseModel
            uuid
            is_active
            created_at
            modified_at
    """

    name_provider = models.CharField(
        max_length=255,
        null=False,
        unique=True,
    )
    nit_provider = models.CharField(
        max_length=11, null=False, unique=True, validators=[validate_nit]
    )
    name_contact_person = models.CharField(max_length=255, null=False)
    number_contact_person = models.CharField(max_length=10, null=True, blank=True)
    number_account_banking = models.CharField(max_length=15, null=False, blank=True)
    bank = models.ForeignKey(
        "applications_banks.Banks",
        on_delete=models.CASCADE,
        related_name="banks_provider_related",
    )

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __str__(self):
        return self.name_provider
