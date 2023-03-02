from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User  
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User  
		fields = ['username', 'email']
		
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['school_name', 'logo', 'banner', 'contact_details', 'mapbox_key', 'event_markers_dataset_link', 'newgame_markers_dataset_link', 'health_markers_dataset_link', 'food_markers_dataset_link', 'finance_markers_dataset_link', 'store_markers_dataset_link', 'etc_markers_dataset_link', 'newgame_textfield', 'live_chat_link', 'chatbot_tree_link']


class MainUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['school_name', 'logo', 'banner']