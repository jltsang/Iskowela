from django.shortcuts import render, redirect
from users.models import Profile
from users.forms import MainUpdateForm
from .models import Toggles, Post
from django.contrib import messages
from django.views.generic import (
	CreateView, 
	UpdateView, 
	DeleteView
)

active_profile = Profile.objects.get(id=1)

def index(request):
	context = {
		'active_profile': active_profile,
		'toggles': Toggles.objects.get(profile = 1),
		'title': 'Home',
		'posts': Post.objects.all()
	}
	return render(request, 'main/index.html', context)

def menu(request):
	context = {
		'title': 'Menu',
		'active_profile': active_profile,
		'toggles': Toggles.objects.get(profile = 1),
	}
	return render(request, 'main/menu.html', context)

def imap_menu(request):
	context = {
		'title': 'Interactive Map Menu',
		'active_profile': active_profile,
		'toggles': Toggles.objects.get(profile = 1),
	}
	return render(request, 'main/imap_menu.html', context)

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
	
	success_url = "/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Settings'
		context['toggles'] = Toggles.objects.get(profile = 1)
		
		return context
	
class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'content', 'author']
	success_url = "/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Post List'

		return context

class PostUpdateView(UpdateView):
	model = Post
	fields = ['title', 'content']
	success_url = "/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Post List'
				
		return context

class PostDeleteView(DeleteView):
	model = Post
	success_url = "/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Post List'
		
		return context
