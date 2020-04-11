from django.db import models
from django.urls import reverse
from django.utils import timezone

class SSR(models.Model):
	Rating_choices = (
	    (1, 'Bad'),
	    (2, 'Poor'),
	    (3, 'Average'),
	    (4, 'Good'),
	    (5, 'Excellent')
	)
	email = models.EmailField()
	interactive_map_comment = models.TextField(default='')
	interactive_map_rating = models.IntegerField(choices=Rating_choices, default=3)
	chatbot_comment = models.TextField(default='')
	chatbot_rating = models.IntegerField(choices=Rating_choices, default=3)
	overall_comment = models.TextField(default='')
	overall_rating = models.IntegerField(choices=Rating_choices, default=3)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.email

	def get_absolute_url(self):
		return reverse('ssr-create')