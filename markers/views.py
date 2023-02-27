from django.shortcuts import render
from .models import Event_Markers, Event_Suggestions, Place_Markers, Place_Suggestions
from main.models import Toggles
from django.urls import reverse
from django.views.generic import (
	CreateView, 
	UpdateView, 
	DeleteView
)
from django.forms import DateTimeInput

def markers(request, mtype):
	context = {
		'title': 'Markers',
		'mtype': mtype,
		'places': Place_Markers.objects.all(),
		'toggles': Toggles.objects.get(school_name="Roosevelt College Marikina")
	}
	return render(request, 'markers/map.html', context)
	
class EventCreateView(CreateView):
	model = Event_Markers
	fields = ['name', 'type', 'description', 'event_date', 'latitude', 'longitude'] 
	success_url = "/markers/1"
	
	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['latitude'].widget = form.fields['latitude'].hidden_widget()
		form.fields['longitude'].widget = form.fields['longitude'].hidden_widget()
		form.fields['event_date'].widget = DateTimeInput(attrs={'type': 'datetime-local'})

		return form

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Markers'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context
	
class EventUpdateView(UpdateView):
	model = Event_Markers
	fields = ['name', 'type', 'description', 'event_date', 'longitude', 'latitude']
	success_url = "/markers/1"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Markers'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context
	
class EventDeleteView(DeleteView):
	model = Event_Markers
	success_url = "/markers/1"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Markers'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")

		return context

class PlaceCreateView(CreateView):
	model = Place_Markers
	fields = ['name', 'type', 'description', 'latitude', 'longitude']
	success_url = "/markers/2"
	
	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['latitude'].widget = form.fields['latitude'].hidden_widget()
		form.fields['longitude'].widget = form.fields['longitude'].hidden_widget()
		return form

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Markers'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context
	
class PlaceUpdateView(UpdateView):
	model = Place_Markers
	fields = ['name', 'type', 'description', 'longitude', 'latitude']
	success_url = "/markers/2"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Process Guides'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context
	
class PlaceDeleteView(DeleteView):
	model = Place_Markers
	success_url = "/markers/2"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context