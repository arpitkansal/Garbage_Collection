from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Driver, Residents, Area
from fcm_django.fcm import fcm_send_topic_message

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def fetchPath(request, driver_id):
    qs =  Area.objects.filter(driver_id = driver_id)
    path = []
    for i in qs:
        area = dict()
        area["id"] = i.area_id
        area["name"] = i.name
        area["lats"] = i.lats
        area["longs"] = i.longs
        path.append(area)
    return JsonResponse(path, safe=False)


def alertResident(request , rid):
    return JsonResponse({rid:'yes'})

def fetchReached(request, driver_id, area_id):

    list = []
    qs = Residents.objects.filter(area_id = area_id)
    for i in qs:
        list.append(i.res_id)
    for i in list:
        url = "/garbage/alertResident/" + str(i)
        response = redirect(url)
        return response

def fetchArea(request):
    qs = Area.objects.all()
    path = []
    for i in qs:
        area = dict()
        area["id"] = i.area_id
        area["name"] = i.name
        path.append(area)
    return JsonResponse(path, safe=False)

def notifyResidents(request,topic_name):

   k = fcm_send_topic_message(topic_name=topic_name, message_body='The vehicle has arrived in your area',
                              message_title=topic_name)
   return JsonResponse(list(k))
