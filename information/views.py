from django.shortcuts import render
from .models import ProcessGuide, Courses, Scholarships
from django.urls import reverse
from django.views.generic import (
	CreateView, 
	UpdateView, 
	DeleteView
)

def processguide_list(request):
	context = {
		'title': 'Process Guides',
		'processguides': ProcessGuide.objects.all(),
	}
	return render(request, 'information/processguides.html', context)

def course_list(request):
	context = {
		'title': 'Course List',
		'courses': Courses.objects.all(),
	}
	return render(request, 'information/courses.html', context)

def scholarship_list(request):
	context = {
		'title': 'Scholarships',
		'scholarships': Scholarships.objects.all(),
	}
	return render(request, 'information/scholarships.html', context)

class ProcessGuidesCreateView(CreateView):
	model = ProcessGuide
	fields = ['process_name', 'description']
	success_url = "/processguides/"

class ProcessGuidesUpdateView(UpdateView):
	model = ProcessGuide
	fields = ['process_name', 'description']

class ProcessGuidesDeleteView(DeleteView):
	model = ProcessGuide
	success_url = "/processguides/"

class ScholarshipsCreateView(CreateView):
	model = Scholarships
	fields = ['scholarship_name', 'description']
	success_url = "/scholarships/"

class ScholarshipsUpdateView(UpdateView):
	model = Scholarships
	fields = ['scholarship_name', 'description']

class ScholarshipsDeleteView(DeleteView):
	model = Scholarships
	success_url = "/scholarships/"

class CoursesCreateView(CreateView):
	model = Courses
	fields = ['college_group', 'course_list']
	success_url = "/courses/"

class CoursesUpdateView(UpdateView):
	model = Courses
	fields = ['college_group', 'course_list']

class CoursesDeleteView(DeleteView):
	model = Courses
	success_url = "/courses/"