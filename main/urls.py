from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main-index'),
    path('menu', views.menu, name='main-menu'),
]