from django.shortcuts import render, get_object_or_404
from .models import Suggestion
from django.urls import reverse
from users.models import Profile
from main.models import Toggles
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView, 
	DeleteView
)
from django.core.paginator import Paginator
import json
import urllib
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q

def index(request):
	context = {
		'title': 'Interactive Map',
		'suggestions': Suggestion.objects.all(),
		'toggles': Toggles.objects.get(school_name="Roosevelt College Marikina")
	}
	return render(request, 'interactive_map/index.html', context)

def newgame(request):
	context = {
		'title': 'Interactive Map',
		'active_profile': Profile.objects.get(school_name="Roosevelt College Marikina"),
		'toggles': Toggles.objects.get(school_name="Roosevelt College Marikina")
	}
	return render(request, 'interactive_map/newgame.html', context)

class SuggestionListView(ListView):
	model = Suggestion
	template_name = 'interactive_map/index.html'
	context_object_name = 'suggestions'
	paginate_by = 3

	def get_queryset(self):
		arg = self.kwargs.get('stype')
		if arg == 1:
			return Suggestion.objects.filter(stype=arg).order_by('-date_posted')
		elif arg == 2:
			return Suggestion.objects.filter(~Q(stype = 1)).order_by('-date_posted')
		else:
			return Suggestion.objects.order_by('-date_posted')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['arg'] = self.kwargs.get('stype')
		context['active_profile'] = Profile.objects.get(school_name="Roosevelt College Marikina")
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")

		if self.kwargs.get('stype') == 1:
			context['layer'] = 'roosevelt-events'
			context['html'] = "'<p>Name: ' + feature.properties.name + '</p><p>Schedule: ' + feature.properties.date + '</p><p>Time:: ' + feature.properties.time + '</p><p>Target Population: ' + feature.properties.target_population"
		else:
			context['layer'] = ['roosevelt-food', 'roosevelt-health', 'roosevelt-finance', 'roosevelt-store']
			context['html'] = "'<p>' + feature.properties.Name + '</p><p>' + feature.properties.Address + '</p><p>' + feature.properties.Contact + '</p><p>' + feature.properties.Hours"
			
		return context

class SuggestionDetailView(DetailView):
	model = Suggestion

class SuggestionCreateView(CreateView):
	model = Suggestion
	fields = ['desc', 'cud', 'stype', 'prev_name', 'name', 'prev_latitude', 'prev_longitude', 'latitude', 'longitude']
	def form_valid(self, form):
		''' Begin reCAPTCHA validation '''
		request = self.request
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
		    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		    'response': recaptcha_response
		}
		data = urllib.parse.urlencode(values).encode()
		req =  urllib.request.Request(url, data=data)
		response = urllib.request.urlopen(req)
		result = json.loads(response.read().decode())
		''' End reCAPTCHA validation '''

		if result['success']:
			form.save()
			messages.success(request, 'New Suggestion added with success!')
			return HttpResponseRedirect(reverse('imap-index', kwargs={'stype': '3'}))
		else:
			messages.error(request, 'Invalid reCAPTCHA. Please try again.')
			return HttpResponseRedirect(reverse('suggestion-create'))

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")

		return context

class SuggestionUpdateView(UpdateView):
	model = Suggestion
	fields = ['desc', 'cud', 'stype', 'prev_name', 'name', 'prev_latitude', 'prev_longitude', 'latitude', 'longitude']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context

class SuggestionDeleteView(DeleteView):
	model = Suggestion
	success_url = "/imap/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Interactive Map'
		context['toggles'] = Toggles.objects.get(school_name="Roosevelt College Marikina")
		
		return context