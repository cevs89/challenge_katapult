from typing import Type, TypeVar

from django.db import IntegrityError, transaction
from django.db.models import Model
from django.utils.translation import gettext_lazy as _

from applications.banks.models import Banks
from applications.utils.functions import normalize_frase

T = TypeVar("T", bound=Model)


class BanksService:
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

    def __validate(self, name_bank: str) -> None:
        """normalize utils name"""
        self.name_normalize = normalize_frase(name_bank)

    def __get_queryset(self, id_bank: id) -> None:
        try:
            queryset = Banks.objects.get(pk=id_bank, is_active=True)
        except Banks.DoesNotExist:
            raise ValueError("Banks Doesn't exists")

        self.queryset = queryset

    def __save_banks(self, models) -> None:
        """try save the data in banks"""
        try:
            with transaction.atomic():
                _save_bank = models
                _save_bank.name_bank = self.name_normalize
                _save_bank.save()
        except (Exception, IntegrityError) as e:
            _msg_erros_save = _("Already Exists the bank")
            if "UNIQUE" in e.args[0]:
                raise ValueError(
                    {"name_bank": f"{_msg_erros_save}: {self.name_normalize}"}
                )
            else:
                raise ValueError(str(e))

        self.model_save = _save_bank

    def save(self, **data: dict) -> Type[Model]:
        """Validate the name and declared in  self.name_normalize"""
        self.__validate(data["name"])
        """ save data in Banks """
        self.__save_banks(Banks())
        return self.model_save

    def edit(self, **data: dict):
        """getting the query get()"""
        self.__get_queryset(data["id"])
        """ Validate the name and declared in  self.name_normalize """
        self.__validate(data["name"])
        """  save data in Banks """
        self.__save_banks(self.queryset)
        return self.model_save

    def list(self) -> Type[Model]:
        """List all available banks - is_active = True"""
        return Banks.objects.filter(is_active=True)

    def details(self, id_bank: id) -> Type[Model]:
        """getting the query get()"""
        self.__get_queryset(id_bank)
        return self.queryset

    def delete(self, id_bank: id) -> str:
        """getting the query get()"""
        self.__get_queryset(id_bank)

        try:
            self.queryset.delete()
        except Exception as e:
            raise ValueError(str(e))

        _msg_response = _("it's was delete")
        return f"{self.queryset.name_bank}: {_msg_response}"
