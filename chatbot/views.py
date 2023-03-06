from django.shortcuts import render
from main.models import Toggles
import requests
from datetime import datetime
from analytics.models import HomeMonitor, InfoMonitor, MarkerMonitor, ChatbotMonitor

def index(request):
	# ################# get ip ######################
	# x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	# if x_forwarded_for:
	# 	ip = x_forwarded_for.split(',')[0]
	# else:
	# 	ip = request.META.get('REMOTE_ADDR') 
	# if ip == '127.0.0.1': # Only define the IP if you are testing on localhost.
	# 	ip = '202.92.130.117'
    
	# url = "https://ipxapi.com/api/ip?ip="
	# url += ip
                
	# headers = {
    #     'Accept': "application/json",
    #     'Content-Type': "application/json",
    #     'Authorization': "Bearer 6742|QLoOwndQ45sjffJRgBK45iOPNVoh8tXDtzG7TXpx",
    #     'cache-control': "no-cache"
    # }
                
	# response = requests.request("GET", url, headers=headers)
	# rawData = response.json()
    
	# continent = rawData["continentName"]
	# country = rawData['country']
	# city = rawData['city']
	# now = datetime.now()  
    # #datetimenow = now.strftime("%Y-%m-%d %H:%M:%S")
    # #datetimenow = now.strftime("%Y-%m-%d")
	# saveNow = ChatbotMonitor(
    #     continent=continent,
    #     country=country,
    #     city=city,
    #     datetime=now,
    #     ip=ip
    # )
	# saveNow.save()
	# ################# get ip ######################
	return render(request, 'chatbot/index.html', {'title': 'Chatbot', 'toggles': Toggles.objects.get(profile = 1)})