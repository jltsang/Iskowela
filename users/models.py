from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	school_name = models.CharField(max_length=40)
	logo = models.ImageField(default='default.jpg', upload_to='logo_pics')
	contact_details = models.TextField()
	mapbox_key = models.CharField(max_length=100)
	new_game_dataset_link = models.CharField(max_length=80)
	event_markers_dataset_link = models.CharField(max_length=80)
	place_markers_dataset_link = models.CharField(max_length=80)
	live_chat_link = models.CharField(max_length=50)
	chatbot_tree_link = models.CharField(max_length=50)

	def __str__(self):
		return f'{self.user.username} Profile'