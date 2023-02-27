from django.urls import path
from rest_framework.authtoken import views

from applications.api.views import RegistrationView

urlpatterns = [
    path("login/", views.obtain_auth_token, name="users_login"),
    path("register/", RegistrationView.as_view(), name="users_register"),
]
