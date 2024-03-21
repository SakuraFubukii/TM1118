from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from iot.models import Event

def index(request):
    return render(request, 'dashboard/index.html')

def temp_data(request):
    events = Event.objects.all()
    data = serializers.serialize('json', events) 
    return JsonResponse(data, safe=False)