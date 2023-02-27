from typing import Type, TypeVar

from django.db.models import Model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from applications.accounts.models import User

T = TypeVar("T", bound=Model)


class RegistrationSerializer(serializers.ModelSerializer):
    """
    I've use the serializer Django like ModelSerializer, cause it's the better way
    for this purpose, but for the others endpoint we'll use Serpy serializers

    Data Recive:
    {
    "email": "carlos.velazquez@example.com",
    "password": "katapult123",
    "password2": "katapult123"
    }

    email: str
    password: str -> write_only
    password2: str -> write_only | Comparison

    We need the password2 just for the comparison with password, it's declared with
    serializers.CharField

    """

    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs: dict) -> dict:
        """Validate password match"""
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match"}
            )

        return attrs

    def get_token(self, _user: Type[T]) -> str:
        """obtain token, after user was create"""
        token, created = Token.objects.get_or_create(user=_user)
        return token.key

    def save(self) -> Type[Model]:
        """Save data in models User"""
        query_save_user = User(email=self.validated_data["email"])
        password = self.validated_data["password"]
        query_save_user.set_password(password)
        query_save_user.save()

        return query_save_user
