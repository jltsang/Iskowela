from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class ProcessGuide(models.Model):
    school_name = models.TextField(default='Roosevelt College Marikina')
    process_name = models.TextField(default='')
    description = models.TextField(default='')
    last_updated = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.process_name
    
    def get_absolute_url(self):
        return reverse('processguides')

class Courses(models.Model):
    schoolid = models.TextField()
    college_group = models.TextField(default='')
    course_list = models.JSONField(default=dict)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.college_group

    def get_absolute_url(self):
        return reverse('courses')

class Scholarships(models.Model):
    schoolid = models.TextField()
    scholarship_name = models.TextField(default='')
    description = models.TextField(default='')
    last_updated = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.scholarship_name

    def get_absolute_url(self):
        return reverse('scholarships')