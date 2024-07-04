from django.urls import path
from .views import *
urlpatterns = [
    path('', tao_admin, name='tao_admin'),
]
