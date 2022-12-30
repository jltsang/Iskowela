from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ProcessGuide, Courses, Scholarships
from django.urls import reverse
from django.views.generic import (
	CreateView, 
	UpdateView, 
	DeleteView
)

def processguides(request):
	context = {
		'title': 'Process Guides',
		'processguides': ProcessGuide.objects.all(),
	}
	return render(request, 'information/processguides.html', context)

def courses(request):
	context = {
		'title': 'Course List',
	}
	return render(request, 'information/courses.html', context)

def scholarships(request):
	context = {
		'title': 'Scholarships',
	}
	return render(request, 'information/scholarships.html', context)

class ProcessGuidesCreateView(CreateView):
	model = ProcessGuide
	fields = ['process', 'description']
	success_url = "/processguides/"

class ProcessGuidesUpdateView(UpdateView):
	model = ProcessGuide
	fields = ['process', 'description']

class ProcessGuidesDeleteView(DeleteView):
	model = ProcessGuide
	success_url = "/processguides/"

# Create your views here.
