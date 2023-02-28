from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from applications.api.serializers import BanksSerializer
from applications.api.validators import ValidateBanks
from applications.banks.service import BanksService


class BanksViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    service = BanksService()
    serializer_class = BanksSerializer
    validations_class = ValidateBanks

    def list(self, request):
        """Method GET"""
        try:
            """get all available banks"""
            queryset = self.service.list()
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        # Serializer Data Response
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Method POST"""
        get_validation = self.validations_class(request.data)
        if get_validation.validate():
            try:
                """save data after validate"""
                query_save = self.service.save(**get_validation.data)
            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

            # Serializer Data Response
            serializer = self.serializer_class(query_save)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(get_validation.errors(), status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Method GET with Params"""
        try:
            """get all available banks"""
            queryset = self.service.details(pk)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        # Serializer Data Response
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        """Method PUT with Params and Body"""
        get_validation = self.validations_class(request.data)
        if get_validation.validate():
            get_validation.data["id"] = pk
            try:
                """edit data after validate"""
                query_edit = self.service.edit(**get_validation.data)
            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

            # Serializer Data Response
            serializer = self.serializer_class(query_edit)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(get_validation.errors(), status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Method Delete with Params"""

        try:
            """get all available banks"""
            _reponse_delete = self.service.delete(pk)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        # Serializer Data Response
        return Response({"msg": _reponse_delete}, status=status.HTTP_200_OK)
