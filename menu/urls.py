from django.urls import path
from . import views
from .views import Menu

urlpatterns = [
    path('', Menu.as_view(), name='menu'),
  ]