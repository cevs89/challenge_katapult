from rest_framework.routers import DefaultRouter

from applications.api.views import ProvidersViewSet

router = DefaultRouter()
router.register("provider", ProvidersViewSet, basename="providers")
urlpatterns = router.urls
