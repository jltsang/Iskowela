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
from django.shortcuts import get_object_or_404

class BaseForm:
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Markers'
		context['toggles'] = Toggles.objects.get(profile = 1)
		
		return context

class EventForm:
	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['latitude'].widget = form.fields['latitude'].hidden_widget()
		form.fields['longitude'].widget = form.fields['longitude'].hidden_widget()
		form.fields['event_date'].widget = DateTimeInput(attrs={'type': 'datetime-local'})

		return form
	
class PlaceForm:
	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['latitude'].widget = form.fields['latitude'].hidden_widget()
		form.fields['longitude'].widget = form.fields['longitude'].hidden_widget()

		return form

def markers(request, mtype):
	context = {
		'title': 'Markers',
		'mtype': mtype,
		'places': Place_Markers.objects.all(),
		'events' : Event_Markers.objects.all(),
		'event_suggestions' : Event_Suggestions.objects.all(),
		'place_suggestions' : Place_Suggestions.objects.all(),
		'toggles': Toggles.objects.get(profile = 1)
	}
	return render(request, 'markers/map.html', context)
	
class EventCreateView(BaseForm, EventForm, CreateView):
	model = Event_Markers
	fields = ['name', 'type', 'description', 'event_date', 'latitude', 'longitude'] 
	success_url = "/markers/1"
	
class EventUpdateView(BaseForm, EventForm, UpdateView):
	model = Event_Markers
	fields = ['name', 'type', 'description', 'event_date', 'longitude', 'latitude']
	success_url = "/markers/1"
	
class EventDeleteView(BaseForm, DeleteView):
	model = Event_Markers
	success_url = "/markers/1"

class PlaceCreateView(BaseForm, PlaceForm, CreateView):
	model = Place_Markers
	fields = ['name', 'type', 'description', 'latitude', 'longitude']
	success_url = "/markers/2"

class PlaceUpdateView(BaseForm, PlaceForm, UpdateView):
	model = Place_Markers
	fields = ['name', 'type', 'description', 'longitude', 'latitude']
	success_url = "/markers/2"
	
class PlaceDeleteView(BaseForm, DeleteView):
	model = Place_Markers
	success_url = "/markers/2"
	
class SuggestEventCreateView(BaseForm, EventForm, CreateView):
	model = Event_Suggestions
	fields = ['cud', 'name', 'type', 'description', 'event_date', 'longitude', 'latitude']
	success_url = "/markers/1"
	
class SuggestPlaceCreateView(BaseForm, PlaceForm, CreateView):
	model = Place_Suggestions
	fields = ['cud', 'name', 'type', 'description', 'longitude', 'latitude']
	success_url = "/markers/2"
	
class SuggestEventDeleteView(BaseForm, DeleteView):
	model = Event_Suggestions
	success_url = "/markers/3"

class SuggestPlaceDeleteView(BaseForm, DeleteView):
	model = Place_Suggestions
	success_url = "/markers/3"


""" Extra Views
class SuggestEventUpdateView(BaseForm, EventForm, UpdateView):
	model = Event_Suggestions
	fields = ['cud', 'name', 'type', 'description', 'event_date', 'longitude', 'latitude']
	success_url = "/markers/3"

class SuggestPlaceUpdateView(BaseForm, PlaceForm, UpdateView):
	model = Place_Suggestions
	fields = ['cud', 'name', 'type', 'description', 'longitude', 'latitude']
	success_url = "/markers/3
"""