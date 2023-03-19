from django.shortcuts import render, redirect
from main.models import Toggles
import requests
from django.utils import timezone
from .models import Monitor, TimeTracking
from django.core.paginator import Paginator
from django.utils import timezone
import datetime
from django.contrib.gis.geoip2 import GeoIP2
from django.db.models import Count
from users.models import Profile
import json
from django.db.models import Sum



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
    # Per Module View Data
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

    page_list = ['Courses', 'Process Guides', 'Scholarships', 'Chatbot', 'Events/Places']
    page_count = [course, process, scholarship, chatbot, markers]

    # Visitor Location Data
    countries = Monitor.objects.filter(profile = profile_id).values('country').distinct()
    country_list = list(countries.values_list('country',flat=True))
    country_count = [Monitor.objects.filter(profile = profile_id, country= country).count() for country in country_list]



    # Overall site visit
    today = timezone.now()
    start_of_month = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    end_of_month = start_of_month.replace(month=start_of_month.month+1)-timezone.timedelta(microseconds=1)

    data = (
        Monitor.objects
        .filter(profile = profile_id, datetime__gte=start_of_month, datetime__lte=end_of_month)
        .values('datetime__date')
        .annotate(ip_count=Count('ip'))
        .order_by('datetime__date')
    )
    
    
    # Time Spent Per Module View Data
    course_time = TimeTracking.objects.filter(page__contains="{}/courses/".format(profile_id)).aggregate(Sum('time_spent'))['time_spent__sum']
    scholarship_time = TimeTracking.objects.filter(page__icontains="{}/scholarships/".format(profile_id)).aggregate(Sum('time_spent'))['time_spent__sum']
    process_time = TimeTracking.objects.filter(page__icontains="{}/processguides/".format(profile_id)).aggregate(Sum('time_spent'))['time_spent__sum']
    chatbot_time = TimeTracking.objects.filter(page__icontains="{}/chatbot/".format(profile_id)).aggregate(Sum('time_spent'))['time_spent__sum']
    marker_time = TimeTracking.objects.filter(page__icontains="{}/markers/".format(profile_id)).aggregate(Sum('time_spent'))['time_spent__sum']
     
    time_spent = [course_time, process_time, scholarship_time, chatbot_time, marker_time]

    context = {'page_list':page_list, 'page_count':page_count, 'country_list': country_list, 'country_count': country_count, 'data': data, 'time_spent': time_spent}
    return context