from django.shortcuts import render
from main.models import Toggles

def index(request):
	return render(request, 'chatbot/index.html', {'title': 'Chatbot', 'toggles': Toggles.objects.get(school_name="Roosevelt College Marikina")})