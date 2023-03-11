from django.contrib import admin
from django.urls import path, include
from .views import CategoryViewSet

from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register(r"category", CategoryViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
