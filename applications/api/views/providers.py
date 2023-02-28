from applications.api.serializers import ProvidersSerializer
from applications.api.validators import ValidateProviders
from applications.core.views import BaseViewSet, ListModelMixin, ResultsSetPagination
from applications.provider.models import Provider
from applications.provider.service import ProviderService


class ProvidersViewSet(ListModelMixin, BaseViewSet):
    service = ProviderService()
    queryset = Provider.objects.all()
    serializer_class = ProvidersSerializer
    validations_class = ValidateProviders
    pagination_class = ResultsSetPagination
