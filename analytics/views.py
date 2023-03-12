from django.shortcuts import render, redirect
from main.models import Toggles
import requests
import time 
import os
from django.utils import timezone
from .models import Monitor, HomeMonitor, InfoMonitor, MarkerMonitor, ChatbotMonitor
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.gis.geoip2 import GeoIP2
from users.models import Profile


#traffic monitor
def traffic_monitor(request, profile_id):
    # dataSaved_info = InfoMonitor.objects.filter(profile = profile_id).order_by('-datetime')
    # dataSaved_marker = MarkerMonitor.objects.filter(profile = profile_id).order_by('-datetime')
    # dataSaved_chatbot = ChatbotMonitor.objects.filter(profile = profile_id).order_by('-datetime')
    # dataSaved_home = HomeMonitor.objects.filter(profile = profile_id).order_by('-datetime')
    dataSaved = Monitor.objects.filter(profile = profile_id).order_by('-datetime')
    
    # totalSiteVisits = dataSaved_info.count() + dataSaved_chatbot.count() + dataSaved_home.count() + dataSaved_marker.count()
    totalSiteVisits = dataSaved.count()
    #unique page viewers
    a = Monitor.objects.order_by().values('ip').distinct()
    pp = Paginator(a, 100)
    unique = (pp.count)
    

    # p = Paginator(dataSaved_info, 100)
    # pageNum = request.GET.get('page', 1)
    # page1 = p.page(pageNum)

    # p = Paginator(dataSaved_marker, 100)
    # pageNum = request.GET.get('page', 1)
    # page2 = p.page(pageNum)

    # p = Paginator(dataSaved_home, 100)
    # pageNum = request.GET.get('page', 1)
    # page3 = p.page(pageNum)

    # p = Paginator(dataSaved_chatbot, 100)
    # pageNum = request.GET.get('page', 1)
    # page4 = p.page(pageNum)
    
    p = Paginator(dataSaved, 100)
    pageNum = request.GET.get('page', 1)
    page = p.page(pageNum)

    #update time
    now = timezone.now()
    data = {
        "now":now,
        "unique":unique,
        "totalSiteVisits":totalSiteVisits,
        "courseVisits": Monitor.objects.filter(page_visited = "course", profile = profile_id).count(),
        "processVisits": Monitor.objects.filter(page_visited = "process", profile = profile_id).count(),
        "scholarshipVisits": Monitor.objects.filter(page_visited = "scholarship", profile = profile_id).count(),
        "markerVisits": Monitor.objects.filter(page_visited = "markers", profile = profile_id).count(),
        "chatbotVisits": Monitor.objects.filter(page_visited = "chatbot", profile = profile_id).count(),
        "userSession": page,
        # "infoSession": page1,
        # "markerSession": page2,
        # "homeSession": page3,
        # "chatbotSession": page4,
    }

    context = {
		'toggles': Toggles.objects.get(profile = profile_id),
        'data': data,
        'profile_id': profile_id,
	}
   

    return render(request, 'analytics/traffic_monitor.html', context)

#home page
def get_ip(request, profile_id, page):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') 
    if ip == '127.0.0.1': # Only define the IP if you are testing on localhost.
        ip = '202.92.130.117'
    
    g = GeoIP2()
    location = g.city(ip)
    

    continent = location["continent_name"]
    country = location["country_name"]
    city = location["city"]

    datetimenow = timezone.now()
  
    # #datetimenow = now.strftime("%Y-%m-%d")
    saveNow = Monitor(
         profile=Profile.objects.get(id=profile_id),
         continent=continent,
         country=country,
         city=city,
         datetime=datetimenow,
         ip=ip,
        page_visited=page
     )
    saveNow.save()
    