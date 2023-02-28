from rest_framework.routers import DefaultRouter

from applications.api.views import BanksViewSet

router = DefaultRouter()
router.register("banks", BanksViewSet, basename="banks")
urlpatterns = router.urls
