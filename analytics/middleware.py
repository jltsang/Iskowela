from django.utils import timezone
from .models import TimeTracking

class TimeTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)
        
        # Only track time for GET requests
        if request.method == 'GET':
            # Check if the user is authenticated
            if request.user.is_authenticated:
                # Get or create the TimeTracking object
                try:
                    time_tracking = TimeTracking.objects.get(user=request.user, page=request.path)
                except TimeTracking.DoesNotExist:
                    time_tracking = TimeTracking(user=request.user, page=request.path)
            
                # Record the current time
                time_tracking.start_time = timezone.now()
                time_tracking.save()
            
        return response

class TimeTrackingUpdateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)
        
        # Only update time for GET requests
        if request.method == 'GET':
            # Check if the user is authenticated
            if request.user.is_authenticated:
                # Get the TimeTracking object for the current page
                try:
                    time_tracking = TimeTracking.objects.get(user=request.user, page=request.path)
                except TimeTracking.DoesNotExist:
                    return response
            
                # Calculate the time spent on the page
                time_spent = (timezone.now() - time_tracking.start_time).total_seconds()
            
                # Update the TimeTracking object
                time_tracking.time_spent = time_spent
                time_tracking.save()
            
        return response
