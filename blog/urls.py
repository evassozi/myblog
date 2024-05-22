from django.contrib import admin
from django.urls import path
from .views import home, details

urlpatterns = [
   path(route='', view=home),
   path(route='<int:id>', view=details)
]
