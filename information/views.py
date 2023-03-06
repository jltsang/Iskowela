from django.shortcuts import render , redirect
from .models import ProcessGuide, Courses, Scholarships
from main.models import Toggles
from django.urls import reverse
import requests
from datetime import datetime
from analytics.models import HomeMonitor, InfoMonitor, MarkerMonitor, ChatbotMonitor
from django.views.generic import (
	CreateView, 
	UpdateView, 
	DeleteView
)


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

class BaseView:
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Markers'
		context['toggles'] = Toggles.objects.get(profile = 1)
		
		return context

def processguide_list(request):
	# get_ip_info(request)
	context = {
		'title': 'Process Guides',
		'processguides': ProcessGuide.objects.all(),
		'toggles': Toggles.objects.get(profile = 1),
	}
	return render(request, 'information/processguides.html', context)

def course_list(request):
	# get_ip_info(request)
	context = {
		'title': 'Course List',
		'courses': Courses.objects.all(),
		'toggles': Toggles.objects.get(profile = 1),
	}
	return render(request, 'information/courses.html', context)

def scholarship_list(request):
	# get_ip_info(request)
	context = {
		'title': 'Scholarships',
		'scholarships': Scholarships.objects.all(),
		'toggles': Toggles.objects.get(profile = 1),
	}
	return render(request, 'information/scholarships.html', context)

class ProcessGuidesCreateView(BaseView, CreateView):
	model = ProcessGuide
	fields = ['process_name', 'description']
	success_url = "/processguides/"

class ProcessGuidesUpdateView(BaseView, UpdateView):
	model = ProcessGuide
	fields = ['process_name', 'description']

class ProcessGuidesDeleteView(BaseView, DeleteView):
	model = ProcessGuide
	success_url = "/processguides/"

class ScholarshipsCreateView(BaseView, CreateView):
	model = Scholarships
	fields = ['scholarship_name', 'description']
	success_url = "/scholarships/"

class ScholarshipsUpdateView(BaseView, UpdateView):
	model = Scholarships
	fields = ['scholarship_name', 'description']

class ScholarshipsDeleteView(BaseView,DeleteView):
	model = Scholarships
	success_url = "/scholarships/"

class CoursesCreateView(BaseView, CreateView):
	model = Courses
	fields = ['college_group', 'course_list']
	success_url = "/courses/"

class CoursesUpdateView(BaseView, UpdateView):
	model = Courses
	fields = ['college_group', 'course_list']

class CoursesDeleteView(BaseView, DeleteView):
	model = Courses
	success_url = "/courses/"