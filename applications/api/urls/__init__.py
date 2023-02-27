from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path(
        "accounts/",
        include("applications.api.urls.register_user"),
    ),
]
