from typing import Type, TypeVar

from django.db.models import Model

from applications.banks.models import Banks
from applications.core.views import BaseService

T = TypeVar("T", bound=Model)


class BanksService(BaseService):
    """
    AbstracClass: BaseService

    modify the properties unique for Banks
    """

    def save(self, **data: dict) -> Type[Model]:
        """Validate the name and declared in  self.name_normalize"""
        self._validate(data["name"])
        """ save data in Banks """
        self._save_models_data(Banks())
        return self.model_save

    def edit(self, **data: dict):
        """getting the query get()"""
        self._get_queryset(data["id"])
        """ Validate the name and declared in  self.name_normalize """
        self._validate(data["name"])
        """  save data in Banks """
        self._save_models_data(self.queryset)
        return self.model_save
