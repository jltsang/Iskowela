from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required #Must be signed in (as admin) in order to create new admin accounts
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

def profile(request):
	context = {
		'title': 'About',
		'active_profile': Profile.objects.get(school_name="Roosevelt College Marikina"),
	}
	return render(request, 'users/profile.html', context)