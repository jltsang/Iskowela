from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.index, name='main-index'),
    path('menu', views.menu, name='main-menu'),
    path('imap_menu', views.imap_menu, name='imap-menu'),
    path('main_update', views.main_update, name='main-update'),
    path('post/new', login_required(views.PostCreateView.as_view()), name='post-create'),
    path('post/delete/<pk>/', login_required(views.PostDeleteView.as_view()), name='post-delete'),
    path('post/update/<pk>/', login_required(views.PostUpdateView.as_view()), name='post-update'),
]