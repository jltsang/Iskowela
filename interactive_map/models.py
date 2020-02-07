from django.db import models
from django.utils import timezone
from django.urls import reverse

class Suggestion(models.Model):
	class EventPlace(models.IntegerChoices):
		EVENT = 1
		PLACE = 2
	class Action(models.IntegerChoices):
		CREATE = 1
		UPDATE = 2
		DELETE = 3
	desc = models.CharField(max_length=100, unique=True)
	stype = models.IntegerField(choices=EventPlace.choices)
	prev_name = models.CharField(max_length=100, default=None, blank=True)
	name = models.CharField(max_length=100)
	prev_longitude = models.DecimalField(default=0, decimal_places=6, max_digits=9)
	prev_latitude = models.DecimalField(default=0, decimal_places=6, max_digits=8)
	longitude = models.DecimalField(default=0, decimal_places=6, max_digits=9)
	latitude = models.DecimalField(default=0, decimal_places=6, max_digits=8)
	cud = models.IntegerField(choices=Action.choices)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.desc

	def get_absolute_url(self):
		return reverse('imap-index', kwargs={'stype': '3'})