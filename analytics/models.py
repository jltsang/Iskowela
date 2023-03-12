from django.db import models
from users.models import Profile


class Monitor(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    page_visited = models.CharField(max_length=50, blank=True, null=True)
    continent = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.ip
    
    
