from django.shortcuts import render, redirect
from main.models import Toggles
import requests
import time 
import os
from datetime import datetime
from .models import HomeMonitor, InfoMonitor, MarkerMonitor, ChatbotMonitor
from django.core.paginator import Paginator
from django.utils import timezone

#traffic monitor
def traffic_monitor(request, profile_id):
    dataSaved_info = InfoMonitor.objects.all().order_by('-datetime')
    dataSaved_marker = MarkerMonitor.objects.all().order_by('-datetime')
    dataSaved_chatbot = ChatbotMonitor.objects.all().order_by('-datetime')
    dataSaved_home = HomeMonitor.objects.all().order_by('-datetime')
    
    totalSiteVisits = dataSaved_info.count() + dataSaved_chatbot.count() + dataSaved_home.count() + dataSaved_marker.count()
    #unique page viewers
    a = HomeMonitor.objects.order_by().values('ip').distinct()
    pp = Paginator(a, 100)
    unique = (pp.count)

    p = Paginator(dataSaved_info, 100)
    pageNum = request.GET.get('page', 1)
    page1 = p.page(pageNum)

    p = Paginator(dataSaved_marker, 100)
    pageNum = request.GET.get('page', 1)
    page2 = p.page(pageNum)

    p = Paginator(dataSaved_home, 100)
    pageNum = request.GET.get('page', 1)
    page3 = p.page(pageNum)

    p = Paginator(dataSaved_chatbot, 100)
    pageNum = request.GET.get('page', 1)
    page4 = p.page(pageNum)
    
    #update time
    now = datetime.now()
    data = {
        "now":now,
        "unique":unique,
        "totalSiteVisits":totalSiteVisits,
        "infoVisits": dataSaved_info.count(),
        "markerVisits": dataSaved_marker.count(),
        "chatbotVisits": dataSaved_chatbot.count(),
        "infoSession": page1,
        "markerSession": page2,
        "homeSession": page3,
        "chatbotSession": page4,
    }

    context = {
		'toggles': Toggles.objects.get(profile = 1),
        'data': data,
        'profile_id': profile_id,
	}
   

    return render(request, 'analytics/traffic_monitor.html', context)

#home page
def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') 
    if ip == '127.0.0.1': # Only define the IP if you are testing on localhost.
        ip = '202.92.130.117'
    
    url = "https://ipxapi.com/api/ip?ip="
    url += ip
                
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': "Bearer 6742|QLoOwndQ45sjffJRgBK45iOPNVoh8tXDtzG7TXpx",
        'cache-control': "no-cache"
    }
                
    response = requests.request("GET", url, headers=headers)
    
    rawData = response.json()
    
    continent = rawData["continentName"]
    country = rawData['country']
    capital = rawData['city'] # to modify
    city = rawData['city']
    now = datetime.now()
    datetimenow = now.strftime("%Y-%m-%d %H:%M:%S")
    #datetimenow = now.strftime("%Y-%m-%d")
    saveNow = HomeMonitor(
        continent=continent,
        country=country,
        city=city,
        datetime=datetimenow,
        ip=ip
    )
    saveNow.save()
    return render(request, 'analytics/home.html')