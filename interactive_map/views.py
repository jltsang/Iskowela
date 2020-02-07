from django.shortcuts import render, get_object_or_404
from .models import Suggestion
from django.urls import reverse
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
		'suggestions': Suggestion.objects.all()
	}
	return render(request, 'interactive_map/index.html', context)

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