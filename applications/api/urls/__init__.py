from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path(
        "accounts/",
        include("applications.api.urls.register_user"),
    ),
    path(
        "",
        include("applications.api.urls.banks"),
    ),
    path(
        "",
        include("applications.api.urls.providers"),
    ),
    path(
        "dashboard/",
        include("applications.api.urls.dasboard"),
    ),
]
