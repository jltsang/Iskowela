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
from markers import views as markers_views
from ssr import views as ssr_views
from users import views as user_views
from main import views as main_views
from portal import views as portal_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', portal_views.SchoolListView.as_view(), name="portal"),
	path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', login_required(auth_views.LogoutView.as_view(template_name='users/logout.html')), name='logout'), #Signed in only

    path('register/', user_views.register, name='register'), #Link to (create new admin)
    path('<int:profile_id>/profile/', user_views.profile, name='profile'),
    path('<int:profile_id>/pupdate/', login_required(user_views.pupdate), name='pupdate'), #Admin only


    # ---------------------------------------------------------------------------------
    path('<int:profile_id>/processguides/', information_views.processguide_list, name='processguides'),
    path('<int:profile_id>/courses/', information_views.course_list, name='courses'),
    path('<int:profile_id>/scholarships/', information_views.scholarship_list, name='scholarships'),

    path('<int:profile_id>/processguides/new', login_required(information_views.ProcessGuidesCreateView.as_view()), name='processguide-create'),
    path('<int:profile_id>/courses/new', login_required(information_views.CoursesCreateView.as_view()), name='courses-create'),
    path('<int:profile_id>/scholarships/new', login_required(information_views.ScholarshipsCreateView.as_view()), name='scholarship-create'),

    path('<int:profile_id>/processguides/update/<pk>/', login_required(information_views.ProcessGuidesUpdateView.as_view()), name='processguide-update'),
    path('<int:profile_id>/courses/update/<pk>/', login_required(information_views.CoursesUpdateView.as_view()), name='courses-update'),
    path('<int:profile_id>/scholarships/update/<pk>/', login_required(information_views.ScholarshipsUpdateView.as_view()), name='scholarship-update'),

    path('<int:profile_id>/processguides/delete/<pk>/', login_required(information_views.ProcessGuidesDeleteView.as_view()), name='processguide-delete'),
    path('<int:profile_id>/courses/delete/<pk>/', login_required(information_views.CoursesDeleteView.as_view()), name='courses-delete'),
    path('<int:profile_id>/scholarships/delete/<pk>/', login_required(information_views.ScholarshipsDeleteView.as_view()), name='scholarship-delete'),

    # ---------------------------------------------------------------------------------
    path('<int:profile_id>/markers/<int:mtype>', markers_views.markers, name='markers'),

    path('<int:profile_id>/markers/new-event', markers_views.EventCreateView.as_view(), name='event-create'),
    path('<int:profile_id>/markers/new-place', markers_views.PlaceCreateView.as_view(), name='place-create'),
    path('<int:profile_id>/markers/suggest-event', markers_views.SuggestEventCreateView.as_view(), name='suggest-event'),
    path('<int:profile_id>/markers/suggest-place', markers_views.SuggestPlaceCreateView.as_view(), name='suggest-place'),

    path('<int:profile_id>/markers/2/<int:pk>/update/', markers_views.PlaceUpdateView.as_view(), name='place-update'),
    path('<int:profile_id>/markers/1/<int:pk>/update/', markers_views.EventUpdateView.as_view(), name='event-update'),
    # path('markers/3/<int:pk>/update/', markers_views.SuggestEventUpdateView.as_view(), name='suggest-event-update'),
    # path('markers/4/<int:pk>/update/', markers_views.SuggestPlaceUpdateView.as_view(), name='suggest-place-update'),

    path('<int:profile_id>/markers/2/<int:pk>/delete/', markers_views.PlaceDeleteView.as_view(), name='place-delete'),
    path('<int:profile_id>/markers/1/<int:pk>/delete/', markers_views.EventDeleteView.as_view(), name='event-delete'),
    path('<int:profile_id>/markers/3/<int:pk>/delete/', markers_views.SuggestEventDeleteView.as_view(), name='suggest-event-delete'),
    path('<int:profile_id>/markers/4/<int:pk>/delete/', markers_views.SuggestPlaceDeleteView.as_view(), name='suggest-place-delete'),

    # ---------------------------------------------------------------------------------
    path('<int:profile_id>/chatbot/', chatbot_views.index, name='chatbot-index'),
    path('<int:profile_id>/settings/<int:pk>', login_required(main_views.SettingsUpdateView.as_view()), name='settings'), 

    # ---------------------------------------------------------------------------------
    path('<int:profile_id>/ssr/', login_required(ssr_views.SSRListView.as_view()), name='ssr-index'), #Admin only
    path('<int:profile_id>/ssr/new', ssr_views.SSRCreateView.as_view(), name='ssr-create'),
    path('<int:profile_id>/ssr/<int:pk>/delete/', login_required(ssr_views.SSRDeleteView.as_view()), name='ssr-delete'), #Admin only
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)