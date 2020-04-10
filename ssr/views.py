from django.shortcuts import render, get_object_or_404
from .models import SSR
from django.urls import reverse
from django.views.generic import (
	ListView, 
	CreateView,
	DeleteView
)
from django.core.paginator import Paginator
from django.db.models import Avg

def index(request):
	context = {
		'title': 'Stats',
		'ratings': SSR.objects.all(),
	}
	return render(request, 'ssr/index.html', context)

class SSRListView(ListView):
	model = SSR
	template_name = 'ssr/index.html'
	context_object_name = 'ssrs'
	paginate_by = 5

	def get_queryset(self):
		return SSR.objects.order_by('-date_posted')

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['title'] = 'Stats'
	    context['average_imap'] = list(SSR.objects.aggregate(Avg('interactive_map_rating')).values())[0]
	    context['average_chatbot'] = list(SSR.objects.aggregate(Avg('chatbot_rating')).values())[0]
	    context['average_overall'] = list(SSR.objects.aggregate(Avg('overall_rating')).values())[0]
	    context['count'] = SSR.objects.count()
	    return context

class SSRCreateView(CreateView):
	model = SSR
	fields = ['email', 'interactive_map_comment', 'interactive_map_rating', 'chatbot_comment', 'chatbot_rating', 'overall_comment', 'overall_rating']

class SSRDeleteView(DeleteView):
	model = SSR
	success_url = "/ssr/"
