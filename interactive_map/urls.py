from django.urls import path
from . import views

urlpatterns = [
    path('', SuggestionListView.as_view(), name='index'),
]