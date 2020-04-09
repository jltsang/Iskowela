from django.shortcuts import render
from users.models import Profile

active_profile = Profile.objects.get(school_name="Roosevelt College Marikina")

def index(request):
	context = {
		'active_profile': active_profile,
	}
	return render(request, 'main/index.html', context)

def menu(request):
	context = {
		'title': 'Menu',
		'active_profile': active_profile,
	}
	return render(request, 'main/menu.html', context)

def imap_menu(request):
	context = {
		'title': 'Interactive Map Menu',
		'active_profile': active_profile,
	}
	return render(request, 'main/imap_menu.html', context)