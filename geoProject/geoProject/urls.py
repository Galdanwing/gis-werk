from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from geoProject.viewsets import UserViewSet
from geoWorld.views import MunicipalityViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"municipalities", MunicipalityViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
