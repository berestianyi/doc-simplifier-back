from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'fop', views.FOPViewSet, basename='fop')
router.register(r'tov', views.TOVViewSet, basename='tov')


urlpatterns = [
    path('', include(router.urls)),
]
