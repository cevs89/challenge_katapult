from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.banks.models import Banks
from applications.provider.models import Provider


class DashboardView(APIView):
    permission_classes = (IsAuthenticated,)
    context_response = {}

    """
    Keep simple this page, cause it's just count ORM fill,
    but may be make better in other statistics or order count stuff.

    """

    def _count_statistics(self) -> None:
        """
        In this case could made this query just with the User Relations,
        But we don't have!
        """
        query_provider = Provider.objects.select_related("bank").all().values("id")
        query_bank = Banks.objects.all().values("id")
        self.context_response["providers"] = len(query_provider)
        self.context_response["banks"] = len(query_bank)

    def get(self, request) -> Response:
        self._count_statistics()
        return Response(
            {"statistics": self.context_response}, status=status.HTTP_200_OK
        )
