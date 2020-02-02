from django.shortcuts import render
from .models import Suggestion
from django.views.generic import ListView

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
	ordering = ['-date_posted']