from django.shortcuts import render
from main.models import Toggles

def index(request):
	return render(request, 'chatbot/index.html', {'title': 'Chatbot', 'toggles': Toggles.objects.get(profile = 1)})