from typing import Type, TypeVar

from django.db import IntegrityError, transaction
from django.db.models import Model
from django.utils.translation import gettext_lazy as _

from applications.banks.models import Banks
from applications.utils.functions import normalize_frase

T = TypeVar("T", bound=Model)


class BaseService:
    """
    Servce with method about manage the Banks Models.

    It's pretty intuitive but....
        save: Save the data in models Banks
        edit: Edit existing data in models Banks
        list: Show all available banks - is_active = True
        details: Show the dealts to the single bank
        delete: Delete definitely a single bank

    """

    def __init__(self) -> None:
        self.queryset: Type[T] = None
        self.model_save: Type[T] = None
        self.name_normalize: str = None

    def _get_query_all(self):
        """List all available banks - is_active = True"""
        return Banks.objects.filter(is_active=True)

    def _validate(self, name_bank: str) -> None:
        """normalize utils name"""
        self.name_normalize = normalize_frase(name_bank)

    def _get_queryset(self, id_obj: id) -> None:
        try:
            queryset = Banks.objects.get(pk=id_obj, is_active=True)
        except Banks.DoesNotExist:
            raise ValueError("Banks Doesn't exists")

        self.queryset = queryset

    def _save_models_data(self, models, **data) -> None:
        """try save the data in banks"""
        try:
            with transaction.atomic():
                _save_bank = models
                _save_bank.name_bank = self.name_normalize
                _save_bank.save()
        except (Exception, IntegrityError) as e:
            _msg_erros_save = _("Already Exists")
            if "UNIQUE" in e.args[0]:
                raise ValueError(
                    {"name_bank": f"{_msg_erros_save}: {self.name_normalize}"}
                )
            else:
                raise ValueError(str(e))

        self.model_save = _save_bank

    def save(self, **data: dict) -> Type[Model]:
        pass

    def edit(self, **data: dict):
        """getting the query get()"""
        self._get_queryset(data["id"])
        """  save data in Obj """
        self._save_models_data(self.queryset, **data)
        return self.model_save

    def list(self) -> Type[Model]:
        """List all available banks - is_active = True"""
        return self._get_query_all()

    def details(self, id_obj: id) -> Type[Model]:
        """getting the query get()"""
        self._get_queryset(id_obj)
        return self.queryset

    def delete(self, id_obj: id) -> str:
        """getting the query get()"""
        self._get_queryset(id_obj)

        try:
            self.queryset.delete()
        except Exception as e:
            raise ValueError(str(e))

        _msg_response = _("The record it's was delete")
        return _msg_response
