from django.urls import path

from applications.api.views import DashboardView

urlpatterns = [
    path("view/", DashboardView.as_view(), name="dashboard_view"),
]
