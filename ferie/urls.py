from django.urls import path
from . import views
from .views import Ferie

urlpatterns = [
    path('', Ferie.as_view(), name='ferie'),
]