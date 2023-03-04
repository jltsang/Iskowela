from django.shortcuts import render
from .models import ProcessGuide, Courses, Scholarships
from main.models import Toggles
from django.urls import reverse
from django.views.generic import (
	CreateView, 
	UpdateView, 
	DeleteView
)

class BaseView:
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Markers'
		context['toggles'] = Toggles.objects.get(profile = 1)
		
		return context

def processguide_list(request):
	context = {
		'title': 'Process Guides',
		'processguides': ProcessGuide.objects.all(),
		'toggles': Toggles.objects.get(profile = 1),
	}
	return render(request, 'information/processguides.html', context)

def course_list(request):
	context = {
		'title': 'Course List',
		'courses': Courses.objects.all(),
		'toggles': Toggles.objects.get(profile = 1),
	}
	return render(request, 'information/courses.html', context)

def scholarship_list(request):
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