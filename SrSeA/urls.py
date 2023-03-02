"""
SrSeA URL Configuration

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
from information import views as information_views
from interactive_map import views as interactive_map_views
from markers import views as markers_views
from ssr import views as ssr_views
from users import views as user_views
from main import views as main_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('', include('main.urls')),
    path('chatbot/', chatbot_views.index, name='chatbot-index'),
    path('admin/', admin.site.urls),

    path('processguides/', information_views.processguide_list, name='processguides'),
    path('processguides/new', login_required(information_views.ProcessGuidesCreateView.as_view()), name='processguide-create'),
    path('processguides/update/<pk>/', login_required(information_views.ProcessGuidesUpdateView.as_view()), name='processguide-update'),
    path('processguides/delete/<pk>/', login_required(information_views.ProcessGuidesDeleteView.as_view()), name='processguide-delete'),
    path('courses/', information_views.course_list, name='courses'),
    path('courses/new', login_required(information_views.CoursesCreateView.as_view()), name='courses-create'),
    path('courses/update/<pk>/', login_required(information_views.CoursesUpdateView.as_view()), name='courses-update'),
    path('courses/delete/<pk>/', login_required(information_views.CoursesDeleteView.as_view()), name='courses-delete'),
    path('scholarships/', information_views.scholarship_list, name='scholarships'),
    path('scholarships/new', login_required(information_views.ScholarshipsCreateView.as_view()), name='scholarship-create'),
    path('scholarships/update/<pk>/', login_required(information_views.ScholarshipsUpdateView.as_view()), name='scholarship-update'),
    path('scholarships/delete/<pk>/', login_required(information_views.ScholarshipsDeleteView.as_view()), name='scholarship-delete'),

    path('markers/<int:mtype>', markers_views.markers, name='markers'),
    path('markers/new-event', markers_views.EventCreateView.as_view(), name='event-create'),
    path('markers/1/<int:pk>/update/', markers_views.EventUpdateView.as_view(), name='event-update'),
    path('markers/1/<int:pk>/delete/', markers_views.EventDeleteView.as_view(), name='event-delete'),
    path('markers/new-place', markers_views.PlaceCreateView.as_view(), name='place-create'),
    path('markers/2/<int:pk>/update/', markers_views.PlaceUpdateView.as_view(), name='place-update'),
    path('markers/2/<int:pk>/delete/', markers_views.PlaceDeleteView.as_view(), name='place-delete'),
    path('markers/suggest-event', markers_views.SuggestEventCreateView.as_view(), name='suggest-event'),
    path('markers/suggest-place', markers_views.SuggestPlaceCreateView.as_view(), name='suggest-place'),
    # path('markers/3/<int:pk>/update/', markers_views.SuggestEventUpdateView.as_view(), name='suggest-event-update'),
    # path('markers/4/<int:pk>/update/', markers_views.SuggestPlaceUpdateView.as_view(), name='suggest-place-update'),
    path('markers/3/<int:pk>/delete/', markers_views.SuggestEventDeleteView.as_view(), name='suggest-event-delete'),
    path('markers/4/<int:pk>/delete/', markers_views.SuggestPlaceDeleteView.as_view(), name='suggest-place-delete'),
    path('imap/<int:stype>', interactive_map_views.SuggestionListView.as_view(), name='imap-index'),
    # path('imap/<int:pk>', interactive_map_views.SuggestionDetailView.as_view(), name='suggestion-detail'), #Deletable / Not really
    path('imap/new', interactive_map_views.SuggestionCreateView.as_view(), name='suggestion-create'),
    path('imap/<int:pk>/update/', interactive_map_views.SuggestionUpdateView.as_view(), name='suggestion-update'),
    path('imap/<int:pk>/delete/', interactive_map_views.SuggestionDeleteView.as_view(), name='suggestion-delete'),
    path('imap/newgame', interactive_map_views.newgame, name='imap-newgame'),

    path('register/', user_views.register, name='register'), #Link to (create new admin)
    path('profile/', user_views.profile, name='profile'),
    path('pupdate/', login_required(user_views.pupdate), name='pupdate'), #Admin only

    path('ssr/', login_required(ssr_views.SSRListView.as_view()), name='ssr-index'), #Admin only
    path('ssr/new', ssr_views.SSRCreateView.as_view(), name='ssr-create'),
    path('ssr/<int:pk>/delete/', login_required(ssr_views.SSRDeleteView.as_view()), name='ssr-delete'), #Admin only

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', login_required(auth_views.LogoutView.as_view(template_name='users/logout.html')), name='logout'), #Signed in only
    path('<pk>/update', login_required(main_views.SettingsUpdateView.as_view()), name='settings'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)