
from django.urls import path, include
from . import views

urlpatterns = [
    # name is used to reverse the mapper
    path('', views.index, name='index'),
]
