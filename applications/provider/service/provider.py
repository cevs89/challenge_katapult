from typing import Type, TypeVar

from django.db import IntegrityError, transaction
from django.db.models import Model
from django.utils.translation import gettext_lazy as _

from applications.banks.models import Banks
from applications.core.views import BaseService
from applications.provider.models import Provider
from applications.utils.functions import normalize_frase

T = TypeVar("T", bound=Model)


class ProviderService(BaseService):
    """
    AbstracClass: BaseService

    modify the properties unique for Providers
    """

    def _get_query_banks(self, **data: dict) -> Type[Model]:
        _list_banks = Banks.objects.filter(is_active=True).values_list(
            "name_bank", flat=True
        )
        try:
            query_bank_validate = Banks.objects.get(
                name_bank=normalize_frase(data["bank"])
            )
        except Banks.DoesNotExist:
            raise ValueError(
                f"Banks Doesn't exists: List available: {list(_list_banks)}"
            )

        return query_bank_validate

    def _get_query_all(self):
        """List all available banks - is_active = True"""
        return Provider.objects.filter(is_active=True)

    def _get_queryset(self, id_provider: id) -> None:
        try:
            queryset = Provider.objects.get(pk=id_provider, is_active=True)
        except Provider.DoesNotExist:
            raise ValueError("Providers Doesn't exists")

        self.queryset = queryset

    def _save_models_data(self, models, **data) -> None:
        _banks_query = self._get_query_banks(**data)
        """try save the data in banks"""
        try:
            with transaction.atomic():
                _save_provider = models
                _save_provider.name_provider = data["name_provider"]
                _save_provider.nit_provider = data["nit_provider"]
                _save_provider.name_contact_person = data["name_contact_person"]
                _save_provider.bank = _banks_query

                if "number_contact_person" in data:
                    _save_provider.number_contact_person = (
                        data["number_contact_person"],
                    )

                if "number_account_banking" in data:
                    _save_provider.number_account_banking = (
                        data["number_account_banking"],
                    )

                _save_provider.save()
        except (Exception, IntegrityError) as e:
            _msg_erros_save = _("Provider Already Exists")
            if "UNIQUE" in e.args[0]:
                raise ValueError({"name_provider": f"{_msg_erros_save}"})
            else:
                raise ValueError(str(e))

        self.model_save = _save_provider

    def save(self, **data: dict) -> Type[Model]:
        """save data in Obj"""
        self._save_models_data(Provider(), **data)
        return self.model_save
