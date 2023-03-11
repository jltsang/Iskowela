from django.shortcuts import render
from users.models import Profile
from .models import ProcessGuide, Courses, Scholarships
from main.models import Toggles
from django.urls import reverse_lazy
from django.views.generic import (
	CreateView, 
	UpdateView, 
	DeleteView
)
from django.http import Http404
import requests
from datetime import datetime
from analytics.models import HomeMonitor, InfoMonitor, MarkerMonitor, ChatbotMonitor

def get_ip_info(request):
	################# get ip ######################
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR') 
	if ip == '127.0.0.1': # Only define the IP if you are testing on localhost.
		ip = '202.92.130.117'
    
	url = "https://ipxapi.com/api/ip?ip="
	url += ip
                
	headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': "Bearer 6742|QLoOwndQ45sjffJRgBK45iOPNVoh8tXDtzG7TXpx",
        'cache-control': "no-cache"
    }
                
	response = requests.request("GET", url, headers=headers)
	rawData = response.json()
    
	continent = rawData["continentName"]
	country = rawData['country']
	city = rawData['city']
	now = datetime.now()  
    #datetimenow = now.strftime("%Y-%m-%d %H:%M:%S")
    #datetimenow = now.strftime("%Y-%m-%d")
	saveNow = InfoMonitor(
        continent=continent,
        country=country,
        city=city,
        datetime=now,
        ip=ip
    )
	saveNow.save()
	################# get ip ######################

class BaseForm:
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Information'
		context['toggles'] = Toggles.objects.get(profile_id=self.kwargs['profile_id'])	
		context['profile_id'] = self.kwargs['profile_id']
		context['active_profile'] = Profile.objects.get(id=self.kwargs['profile_id'])

		return context
	
	def get_initial(self):
		initial = super().get_initial()
		initial['profile'] = self.kwargs['profile_id']

		return initial

	def get_object(self, queryset=None):
		obj = super().get_object(queryset=queryset)
		if obj.profile.id != self.kwargs['profile_id']:
			raise Http404("You are not allowed to edit this place.")
		return obj

def processguide_list(request, profile_id):
	# get_ip_info(request)
	context = {
		'title': 'Process Guides',
		'processguides': ProcessGuide.objects.filter(profile = profile_id),
		'toggles': Toggles.objects.get(profile = profile_id),
		'profile_id': profile_id,
		'active_profile': Profile.objects.get(id=profile_id),
	}
	return render(request, 'information/processguides.html', context)

def course_list(request, profile_id):
	# get_ip_info(request)
	context = {
		'title': 'Course List',
		'courses': Courses.objects.filter(profile = profile_id),
		'toggles': Toggles.objects.get(profile = profile_id),
		'profile_id': profile_id,
		'active_profile': Profile.objects.get(id=profile_id),
	}
	return render(request, 'information/courses.html', context)

def scholarship_list(request, profile_id):
	# get_ip_info(request)
	context = {
		'title': 'Scholarships',
		'scholarships': Scholarships.objects.filter(profile = profile_id),
		'toggles': Toggles.objects.get(profile = profile_id),
		'profile_id': profile_id,
		'active_profile': Profile.objects.get(id=profile_id),
	}
	return render(request, 'information/scholarships.html', context)

class ProcessGuidesCreateView(BaseForm, CreateView):
	model = ProcessGuide
	fields = ['profile', 'process_name', 'description']

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['profile'].widget = form.fields['profile'].hidden_widget()

		return form

class ProcessGuidesUpdateView(BaseForm, UpdateView):
	model = ProcessGuide
	fields = ['profile', 'process_name', 'description']

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['profile'].widget = form.fields['profile'].hidden_widget()

		return form

class ProcessGuidesDeleteView(BaseForm, DeleteView):
	model = ProcessGuide
	
	def get_success_url(self):
		return reverse_lazy("processguides", kwargs={"profile_id": self.object.profile.id})

class ScholarshipsCreateView(BaseForm, CreateView):
	model = Scholarships
	fields = ['profile', 'scholarship_name', 'description']

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['profile'].widget = form.fields['profile'].hidden_widget()

		return form

class ScholarshipsUpdateView(BaseForm, UpdateView):
	model = Scholarships
	fields = ['profile', 'scholarship_name', 'description']

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['profile'].widget = form.fields['profile'].hidden_widget()

		return form

class ScholarshipsDeleteView(BaseForm,DeleteView):
	model = Scholarships

	def get_success_url(self):
		return reverse_lazy("scholarships", kwargs={"profile_id": self.object.profile.id})
	
class CoursesCreateView(BaseForm, CreateView):
	model = Courses
	fields = ['profile', 'college_group', 'course_list']

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['profile'].widget = form.fields['profile'].hidden_widget()

		return form

class CoursesUpdateView(BaseForm, UpdateView):
	model = Courses
	fields = ['profile', 'college_group', 'course_list']

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['profile'].widget = form.fields['profile'].hidden_widget()

		return form

class CoursesDeleteView(BaseForm, DeleteView):
	model = Courses

	def get_success_url(self):
		return reverse_lazy("courses", kwargs={"profile_id": self.object.profile.id})