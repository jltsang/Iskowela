from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	school_name = models.CharField(max_length=40)
	logo = models.ImageField(blank=True, upload_to='logo_pics')
	contact_details = models.TextField()
	mapbox_key = models.CharField(max_length=100)
	event_markers_dataset_link = models.CharField(max_length=80)
	newgame_markers_dataset_link = models.CharField(max_length=80, default='')
	health_markers_dataset_link = models.CharField(max_length=80, default='')
	food_markers_dataset_link = models.CharField(max_length=80, default='')
	finance_markers_dataset_link = models.CharField(max_length=80, default='')
	store_markers_dataset_link = models.CharField(max_length=80, default='')
	etc_markers_dataset_link = models.CharField(max_length=80, default='')
	newgame_textfield = models.TextField(default='')
	live_chat_link = models.CharField(max_length=50)
	chatbot_tree_link = models.CharField(max_length=50)

	def __str__(self):
		return f'{self.user.username} Profile'

	# Resize the logo
	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.logo.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.logo.path)
