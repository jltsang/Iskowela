from django.db import models
from django.utils import timezone
from users.models import Profile

class Event_Suggestions(models.Model):
	class EventType(models.IntegerChoices):
		OFFLINE = 1
		ONLINE = 2
	class Action(models.IntegerChoices):
		CREATE = 1
		UPDATE = 2
		DELETE = 3
		
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
	name = models.CharField(max_length=100)
	type = models.IntegerField(choices=EventType.choices)
	description = models.CharField(max_length=100, default='')
	event_date = models.DateTimeField()
	cud = models.IntegerField(choices=Action.choices)
	longitude = models.DecimalField(default=0, decimal_places=20, max_digits=25)
	latitude = models.DecimalField(default=0, decimal_places=20, max_digits=25)
	date_posted = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.name
	
class Event_Markers(models.Model):
	class EventType(models.IntegerChoices):
		OFFLINE = 1
		ONLINE = 2
		
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
	name = models.CharField(max_length=100)
	type = models.IntegerField(choices=EventType.choices)
	description = models.CharField(max_length=100, default='')
	event_date = models.DateTimeField()
	longitude = models.DecimalField(default=0, decimal_places=20, max_digits=25)
	latitude = models.DecimalField(default=0, decimal_places=20, max_digits=25)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class Place_Suggestions(models.Model):
	class PlaceType(models.IntegerChoices):
		HEALTH = 1
		FOOD = 2
		FINANCE = 3
		STORE = 4
		ETC = 5
	class Action(models.IntegerChoices):
		CREATE = 1
		UPDATE = 2
		DELETE = 3
		
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
	name = models.CharField(max_length=100)
	type = models.IntegerField(choices=PlaceType.choices)
	description = models.CharField(max_length=100, default='')
	cud = models.IntegerField(choices=Action.choices)
	longitude = models.DecimalField(default=0, decimal_places=20, max_digits=25)
	latitude = models.DecimalField(default=0, decimal_places=20, max_digits=25)
	date_posted = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.name
	
class Place_Markers(models.Model):
	class PlaceType(models.IntegerChoices):
		HEALTH = 1
		FOOD = 2
		FINANCE = 3
		STORE = 4
		ETC = 5
	
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
	name = models.CharField(max_length=100)
	type = models.IntegerField(choices=PlaceType.choices)
	description = models.CharField(max_length=100, default='')
	longitude = models.DecimalField(default=0, decimal_places=20, max_digits=25)
	latitude = models.DecimalField(default=0, decimal_places=20, max_digits=25)
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name