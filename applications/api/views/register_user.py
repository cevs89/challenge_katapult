from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.api.serializers import RegistrationSerializer


class RegistrationView(APIView):
    """
    keeping simple this part, just creating user and obtain the Token.

    For this purpose it's the best, have the all validations and
    we keep going with the other endpoint.

    Recive data into the models User and validations
    """

    def post(self, request) -> Response:

        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            """call property save() after validations"""
            _save_user = serializer.save()

            """ Modify the reponse array, add Token"""
            return Response(
                {"token": serializer.get_token(_save_user), "user": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
