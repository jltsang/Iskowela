from django.shortcuts import render, redirect
from users.models import Profile
from users.forms import MainUpdateForm
from .models import Toggles, Post
from django.contrib import messages
<<<<<<< HEAD
from django.urls import reverse_lazy
=======
import requests
from datetime import datetime
from analytics.models import HomeMonitor, InfoMonitor, MarkerMonitor, ChatbotMonitor
>>>>>>> 24ffa1bc61fec7f12e07699fc0600742ba6fdaef
from django.views.generic import (
	CreateView, 
	UpdateView, 
	DeleteView
)
from django.http import Http404

class PostForm:
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Post List'
		context['toggles'] = Toggles.objects.get(profile_id=self.kwargs['profile_id'])	
		context['profile_id'] = self.kwargs['profile_id']
		context['active_profile'] = Profile.objects.get(id=self.kwargs['profile_id'])

<<<<<<< HEAD
		return context

	def get_initial(self):
		initial = super().get_initial()
		initial['profile'] = self.kwargs['profile_id']

		return initial

	def get_object(self, queryset=None):
		obj = super().get_object(queryset=queryset)
		if obj.profile.id != self.kwargs['profile_id']:
			raise Http404("You are not allowed to edit this place.")
		
		return obj

def index(request, profile_id):
=======
def index(request):
	# ################# get ip ######################
	# x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	# if x_forwarded_for:
	# 	ip = x_forwarded_for.split(',')[0]
	# else:
	# 	ip = request.META.get('REMOTE_ADDR') 
	# if ip == '127.0.0.1': # Only define the IP if you are testing on localhost.
	# 	ip = '202.92.130.117'
    
	# url = "https://ipxapi.com/api/ip?ip="
	# url += ip
                
	# headers = {
    #     'Accept': "application/json",
    #     'Content-Type': "application/json",
    #     'Authorization': "Bearer 6742|QLoOwndQ45sjffJRgBK45iOPNVoh8tXDtzG7TXpx",
    #     'cache-control': "no-cache"
    # }
                
	# response = requests.request("GET", url, headers=headers)
	# rawData = response.json()
    
	# continent = rawData["continentName"]
	# country = rawData['country']
	# city = rawData['city']
	# now = datetime.now()  
    # #datetimenow = now.strftime("%Y-%m-%d %H:%M:%S")
    # #datetimenow = now.strftime("%Y-%m-%d")
	# saveNow = HomeMonitor(
    #     continent=continent,
    #     country=country,
    #     city=city,
    #     datetime=now,
    #     ip=ip
    # )
	# saveNow.save()
	# ################# get ip ######################

>>>>>>> 24ffa1bc61fec7f12e07699fc0600742ba6fdaef
	context = {
		'active_profile': Profile.objects.get(id=profile_id),
		'title': 'Home',
		'toggles': Toggles.objects.get(profile=profile_id),
		'posts': Post.objects.filter(profile=profile_id),
		'profile_id': profile_id,
		'active_profile': Profile.objects.get(id=profile_id),
	}
	return render(request, 'main/index.html', context)

def main_update(request):
	if request.method == 'POST':
		form = MainUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if form.is_valid() : 
			form.save()
			messages.success(request, f'Your profile has been updated!')
			return redirect('main-index')

	else:
		form = MainUpdateForm(instance=request.user.profile)
		
	context = {
		'form': form,
		'title': 'Profile Update',
	}
	return render(request, 'main/main_update.html', context)

class SettingsUpdateView(UpdateView):
	model = Toggles
	fields = ['processguides_toggle', 'courses_toggle', 'scholarships_toggle', 'markers_toggle', 'chatbot_toggle', 'web_analytics_toggle']
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Settings'
		context['toggles'] = Toggles.objects.get(profile_id=self.kwargs['profile_id'])
		context['profile_id'] = self.kwargs['profile_id']
		context['pk'] = self.kwargs['pk']
		context['active_profile'] = Profile.objects.get(id=self.kwargs['profile_id'])

		return context
	
	def get_object(self, queryset=None):
		obj = super().get_object(queryset=queryset)
		if obj.profile.id != self.kwargs['profile_id']:
			raise Http404("You are not allowed to edit this place.")
		return obj
	
	def get_success_url(self):
		return reverse_lazy('settings', kwargs={'profile_id': self.kwargs['profile_id'], 'pk': self.kwargs['pk']})

class PostCreateView(PostForm, CreateView):
	model = Post
	fields = ['profile', 'title', 'content']

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['profile'].widget = form.fields['profile'].hidden_widget()

		return form
	
class PostUpdateView(PostForm, UpdateView):
	model = Post
	fields = ['profile', 'title', 'content']

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['profile'].widget = form.fields['profile'].hidden_widget()

		return form

class PostDeleteView(PostForm, DeleteView):
	model = Post

	def get_success_url(self):
		return reverse_lazy("main-index", kwargs={"profile_id": self.object.profile.id})

