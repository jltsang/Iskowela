from django.contrib import admin

# Register your models here.
from .models import HomeMonitor, InfoMonitor, MarkerMonitor, ChatbotMonitor
admin.site.register(HomeMonitor)
admin.site.register(InfoMonitor)
admin.site.register(MarkerMonitor)
admin.site.register(ChatbotMonitor)