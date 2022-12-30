from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class ProcessGuide(models.Model):
    school_name = models.TextField()
    process_name = models.TextField(default='')
    description = models.TextField(default='')
    last_updated = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.process
    
    def get_absolute_url(self):
        return reverse('processguides')

class Courses(models.Model):
    schoolid = models.TextField()
    college_group = models.TextField(default='')
    course_list = models.TextField(default='')
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.process

class Scholarships(models.Model):
    schoolid = models.TextField()
    scholarship = models.TextField(default='')
    description = models.TextField(default='')
    last_updated = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.process