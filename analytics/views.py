from django.shortcuts import render, redirect
from main.models import Toggles
import requests
from django.utils import timezone
from .models import Monitor
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.gis.geoip2 import GeoIP2
from users.models import Profile


def traffic_monitor(request, profile_id):
    dataSaved = Monitor.objects.filter(profile = profile_id).order_by('-datetime')

    p = Paginator(dataSaved, 10)
    pageNum = request.GET.get('page', 1)
    page = p.page(pageNum)

    data = {
        "now":timezone.now(),
        "unique":Monitor.objects.filter(profile = profile_id).values('ip').distinct().count(),
        "totalSiteVisits":dataSaved.count(),
        "courseVisits": Monitor.objects.filter(page_visited = "course", profile = profile_id).count(),
        "processVisits": Monitor.objects.filter(page_visited = "process", profile = profile_id).count(),
        "scholarshipVisits": Monitor.objects.filter(page_visited = "scholarship", profile = profile_id).count(),
        "markerVisits": Monitor.objects.filter(page_visited = "markers", profile = profile_id).count(),
        "chatbotVisits": Monitor.objects.filter(page_visited = "chatbot", profile = profile_id).count(),
        "userSession": page,
    }

    charts = chart(request, profile_id)
    context = {
        'active_profile': Profile.objects.get(id=profile_id),
		'toggles': Toggles.objects.get(profile = profile_id),
        'data': data,
        'profile_id': profile_id,
        'charts': charts,
	}
   

    return render(request, 'analytics/traffic_monitor.html', context)

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

    saveNow = Monitor(
         profile=Profile.objects.get(id=profile_id),
         continent=location["continent_name"],
         country=location["country_name"],
         city=location["city"],
         datetime=timezone.now(),
         ip=ip,
         page_visited=page
     )
    saveNow.save()
    

def chart(request, profile_id):
    course = Monitor.objects.filter(page_visited = "course", profile = profile_id).count()
    course = int(course)
   
    scholarship = Monitor.objects.filter(page_visited = "scholarship", profile = profile_id).count()
    scholarship = int(scholarship)

    process = Monitor.objects.filter(page_visited = "process", profile = profile_id).count()
    process = int(process)

    chatbot = Monitor.objects.filter(page_visited = "chatbot", profile = profile_id).count()
    chatbot = int(chatbot)

    markers = Monitor.objects.filter(page_visited = "markers", profile = profile_id).count()
    markers = int(markers)

    countries = Monitor.objects.filter(profile = profile_id).values('country').distinct()
    country_list = list(countries.values_list('country',flat=True))
    country_count = [Monitor.objects.filter(profile = profile_id, country= country).count() for country in country_list]


    page_list = ['Courses', 'Process Guides', 'Scholarships', 'Chatbot', 'Events/Places']
    page_count = [course, process, scholarship, chatbot, markers]
    context = {'page_list':page_list, 'page_count':page_count, 'country_list': country_list, 'country_count': country_count}
    return context