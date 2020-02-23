"""SrSeA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from chatbot import views as chatbot_views
from interactive_map import views as interactive_map_views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', include('main.urls')),
    path('chatbot/', chatbot_views.index, name='chatbot-index'),
    path('imap/<int:stype>', interactive_map_views.SuggestionListView.as_view(), name='imap-index'),
    path('admin/', admin.site.urls),
    path('imap/<int:pk>', interactive_map_views.SuggestionDetailView.as_view(), name='suggestion-detail'), #Deletable / Not really
    path('imap/new', interactive_map_views.SuggestionCreateView.as_view(), name='suggestion-create'),
    path('imap/<int:pk>/update/', interactive_map_views.SuggestionUpdateView.as_view(), name='suggestion-update'),
    path('imap/<int:pk>/delete/', interactive_map_views.SuggestionDeleteView.as_view(), name='suggestion-delete'),
    path('imap/newgame', interactive_map_views.newgame, name='imap-newgame'),
    path('register/', user_views.register, name='register'), #To be hidden by default
    path('profile/', user_views.profile, name='profile'), #To be hidden by default
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
