from django.shortcuts import render
from users.models import Profile
from .models import Toggles
from django.views.generic import (
	UpdateView, 
)

active_profile = Profile.objects.get(school_name="Roosevelt College Marikina")

def index(request):
	context = {
		'active_profile': active_profile,
		'toggles': Toggles.objects.get(school_name="Roosevelt College Marikina")
	}
	return render(request, 'main/index.html', context)

def menu(request):
	context = {
		'title': 'Menu',
		'active_profile': active_profile,
		'toggles': Toggles.objects.get(school_name="Roosevelt College Marikina")
	}
	return render(request, 'main/menu.html', context)

def imap_menu(request):
	context = {
		'title': 'Interactive Map Menu',
		'active_profile': active_profile,
		'toggles': Toggles.objects.get(school_name="Roosevelt College Marikina")
	}
	return render(request, 'main/imap_menu.html', context)

class SettingsUpdateView(UpdateView):
	model = Toggles
	fields = ['processguides_toggle', 'courses_toggle', 'scholarships_toggle', 'markers_toggle', 'chatbot_toggle', 'web_analytics_toggle']
	
	success_url = "/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Settings'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context