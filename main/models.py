from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Toggles(models.Model):
    school_name = models.CharField(max_length=40)
    info_toggle = models.BooleanField(default=False)
    processguides_toggle = models.BooleanField(default=False)
    scholarships_toggle = models.BooleanField(default=False)
    courses_toggle = models.BooleanField(default=False)
    markers_toggle = models.BooleanField(default=False)
    chatbot_toggle = models.BooleanField(default=False)
    web_analytics_toggle = models.BooleanField(default=False)
    
    def __str__(self):
        return self.school_name

class Post(models.Model):
    school_name = models.CharField(max_length=40, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



