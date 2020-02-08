from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main-index'),
    path('menu', views.menu, name='main-menu'),
    path('imap_menu', views.imap_menu, name='imap-menu'),
]