from django.shortcuts import render
from main.models import Toggles
from users.models import Profile

def index(request, profile_id):
	return render(request, 'chatbot/index.html', {'title': 'Chatbot', 'toggles': Toggles.objects.get(profile = profile_id), 'profile_id': profile_id, 'active_profile': Profile.objects.get(id=profile_id),
})