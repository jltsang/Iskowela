from django.shortcuts import render

def index(request):
	return render(request, 'interactive_map/index.html')