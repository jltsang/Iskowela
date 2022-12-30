from django.shortcuts import render
from .models import ProcessGuide, Courses, Scholarships
from django.views.generic import (
	ListView, 
	DetailView, 
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

# Create your views here.
