from applications.api.serializers import BanksSerializer
from applications.api.validators import ValidateBanks
from applications.banks.service import BanksService
from applications.core.views import BaseViewSet


class BanksViewSet(BaseViewSet):
    service = BanksService()
    serializer_class = BanksSerializer
    validations_class = ValidateBanks
