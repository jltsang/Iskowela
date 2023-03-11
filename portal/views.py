from django.shortcuts import render
from django.views.generic import ListView
from users.models import Profile

class SchoolListView(ListView):
	model = Profile
	paginate_by = 15
	template_name = 'portal/portal.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['profiles'] = Profile.objects.all()
		return context