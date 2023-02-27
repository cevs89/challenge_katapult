from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class UserRegisterTestCase(TestCase):
    def setUp(self):
        url_user_register = "/v1/accounts/register/"
        client = APIClient()
        _array_request = {
            "email": "carlos.velazquez@katapult.com",
            "password": "katapult123",
            "password2": "katapult123",
        }
        response = client.post(
            url_user_register,
            _array_request,
        )
        self.response = response
        self._array_request = _array_request
        self.url_user_register = url_user_register

    def test_correct_response_expected_register(self):
        _reponse = self.response.json()
        self.assertEqual(type(self.response.data), dict)
        self.assertTrue("token" in _reponse)
        self.assertTrue("user" in _reponse)
        self.assertTrue("email" in _reponse["user"])

    def test_correct_register_user(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            self.response.json()["user"]["email"], "carlos.velazquez@katapult.com"
        )

    def test_try_duplicate_email_register(self):
        client = APIClient()
        reponse2 = client.post(
            self.url_user_register,
            self._array_request,
        )
        _erros_msg = ["user with this Email Address already exists."]
        self.assertEqual(reponse2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(reponse2.json()["email"], _erros_msg)

    def test_try_unmatch_password_register(self):
        client = APIClient()
        _array_request = {
            "email": "carlos.velazquez@katapult.com",
            "password": "545",
            "password2": "katapult123",
        }
        response = client.post(
            self.url_user_register,
            _array_request,
        )
        _reponse_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            _reponse_json["email"], ["user with this Email Address already exists."]
        )

    def test_data_not_expected_register(self):
        _erros_msg = {
            "email": ["This field is required."],
            "password": ["This field is required."],
            "password2": ["This field is required."],
        }
        client = APIClient()
        _array_request = {
            "hola": "carlos.velazquez@katapult.com",
            "hola1": "545",
            "hola2": "katapult123",
        }
        response = client.post(
            self.url_user_register,
            _array_request,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), _erros_msg)


class UserLoginTestCase(TestCase):
    def setUp(self):
        url_user_register = "/v1/accounts/register/"
        client = APIClient()
        _array_request = {
            "email": "carlos.velazquez@katapult.com",
            "password": "katapult123",
            "password2": "katapult123",
        }
        client.post(
            url_user_register,
            _array_request,
        )

        """ login user """
        url_user_login = "/v1/accounts/login/"
        client = APIClient()
        _array_request_login = {
            "username": "carlos.velazquez@katapult.com",
            "password": "katapult123",
        }
        response = client.post(
            url_user_login,
            _array_request_login,
        )

        self.token = response.json()["token"]
        self.response = response
        self._array_request = _array_request
        self.url_user_login = url_user_login
        self.erros_msg_login = {
            "non_field_errors": ["Unable to log in with provided credentials."]
        }

    def test_correct_login_user(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_incorrect_password_login(self):
        client = APIClient()
        _array_request_login = {
            "username": "noexiste@katapult.com",
            "password": "katapult123",
        }
        response = client.post(
            self.url_user_login,
            _array_request_login,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), self.erros_msg_login)

    def test_incorrect_email_login(self):
        client = APIClient()
        _array_request_login = {
            "username": "carlos.velazquez@katapult.com",
            "password": "estonoesunacontraseña",
        }

        response = client.post(
            self.url_user_login,
            _array_request_login,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), self.erros_msg_login)

    def test_correct_response_expected_login(self):
        self.assertTrue("token" in self.response.json())
