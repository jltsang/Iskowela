from django.shortcuts import render
from .models import ProcessGuide, Courses, Scholarships
from main.models import Toggles
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
		'toggles': Toggles.objects.get(school_name="Roosevelt College Marikina")
	}
	return render(request, 'information/processguides.html', context)

def course_list(request):
	context = {
		'title': 'Course List',
		'courses': Courses.objects.all(),
		'toggles': Toggles.objects.get(school_name="Roosevelt College Marikina")
	}
	return render(request, 'information/courses.html', context)

def scholarship_list(request):
	context = {
		'title': 'Scholarships',
		'scholarships': Scholarships.objects.all(),
		'toggles': Toggles.objects.get(school_name="Roosevelt College Marikina")
	}
	return render(request, 'information/scholarships.html', context)

class ProcessGuidesCreateView(CreateView):
	model = ProcessGuide
	fields = ['process_name', 'description']
	success_url = "/processguides/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context

class ProcessGuidesUpdateView(UpdateView):
	model = ProcessGuide
	fields = ['process_name', 'description']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context

class ProcessGuidesDeleteView(DeleteView):
	model = ProcessGuide
	success_url = "/processguides/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context

class ScholarshipsCreateView(CreateView):
	model = Scholarships
	fields = ['scholarship_name', 'description']
	success_url = "/scholarships/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context

class ScholarshipsUpdateView(UpdateView):
	model = Scholarships
	fields = ['scholarship_name', 'description']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context

class ScholarshipsDeleteView(DeleteView):
	model = Scholarships
	success_url = "/scholarships/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context

class CoursesCreateView(CreateView):
	model = Courses
	fields = ['college_group', 'course_list']
	success_url = "/courses/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context

class CoursesUpdateView(UpdateView):
	model = Courses
	fields = ['college_group', 'course_list']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context

class CoursesDeleteView(DeleteView):
	model = Courses
	success_url = "/courses/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context