from django.shortcuts import render, get_object_or_404, reverse
from .models import SSR
from django.urls import reverse
from django.views.generic import (
	ListView, 
	CreateView,
	DeleteView
)
from django.core.paginator import Paginator
from django.db.models import Avg
import json
import urllib
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect

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
		context['average_imap'] = round(list(SSR.objects.aggregate(Avg('interactive_map_rating')).values())[0], 2)
		context['average_chatbot'] = round(list(SSR.objects.aggregate(Avg('chatbot_rating')).values())[0], 2)
		context['average_overall'] = round(list(SSR.objects.aggregate(Avg('overall_rating')).values())[0], 2)
		context['count'] = SSR.objects.count()
		return context

class SSRCreateView(CreateView):
	model = SSR
	fields = ['email', 'interactive_map_comment', 'interactive_map_rating', 'chatbot_comment', 'chatbot_rating', 'overall_comment', 'overall_rating']

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
			messages.success(request, 'New comment added with success!')
		else:
			messages.error(request, 'Invalid reCAPTCHA. Please try again.')

		return HttpResponseRedirect(reverse('ssr-create'))

class SSRDeleteView(DeleteView):
	model = SSR
	success_url = "/ssr/"
