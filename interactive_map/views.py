from django.shortcuts import render, get_object_or_404
from .models import Suggestion
from django.urls import reverse
from users.models import Profile
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView, 
	DeleteView
)
from django.core.paginator import Paginator

def index(request):
	context = {
		'title': 'Interactive Map',
		'suggestions': Suggestion.objects.all(),
	}
	return render(request, 'interactive_map/index.html', context)

def newgame(request):
	context = {
		'title': 'Interactive Map',
		'active_profile': Profile.objects.get(school_name="Roosevelt College Marikina"),
	}
	return render(request, 'interactive_map/newgame.html', context)

class SuggestionListView(ListView):
	model = Suggestion
	template_name = 'interactive_map/index.html'
	context_object_name = 'suggestions'
	paginate_by = 3

	def get_queryset(self):
		arg = self.kwargs.get('stype')
		if (arg == 1 or arg == 2):
			return Suggestion.objects.filter(stype=arg).order_by('-date_posted')
		else:
			return Suggestion.objects.order_by('-date_posted')

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['title'] = 'Interactive Map'
	    context['arg'] = self.kwargs.get('stype')
	    context['active_profile'] = Profile.objects.get(school_name="Roosevelt College Marikina")
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

class SuggestionUpdateView(UpdateView):
	model = Suggestion
	fields = ['desc', 'cud', 'stype', 'prev_name', 'name', 'prev_latitude', 'prev_longitude', 'latitude', 'longitude']

class SuggestionDeleteView(DeleteView):
	model = Suggestion
	success_url = "/imap/"