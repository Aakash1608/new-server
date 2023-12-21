from django.urls import path, include
from .views import FileViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"file", viewset=FileViewset, basename="file")


urlpatterns = []
urlpatterns += router.urls