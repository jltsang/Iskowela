from django.shortcuts import render

def index(request):
	return render(request, 'main/index.html')

def menu(request):
	return render(request, 'main/menu.html', {'title': 'Menu'})