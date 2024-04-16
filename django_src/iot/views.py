from django.shortcuts import render
from .models import Event
from . import iot_mqtt
def index(request):
    events = Event.objects.all().order_by('-time')
    W311a = Event.objects.filter(loc = 'W311a').order_by('-time')
    W311b = Event.objects.filter(loc = 'W311b').order_by('-time')
    W311_H1 = Event.objects.filter(loc = 'W311-H1').order_by('-time')
    W311_H2 = Event.objects.filter(loc = 'W311-H2').order_by('-time')
    W311_H3 = Event.objects.filter(loc = 'W311-H3').order_by('-time')
    W311d_Z1 = Event.objects.filter(loc = 'W311d-Z1').order_by('-time')
    W311d_Z2 = Event.objects.filter(loc = 'W311d-Z2').order_by('-time')
    context = {'events':events, 'W311a':W311a, 'W311b':W311b, 'W311_H1':W311_H1, \
               'W311_H2':W311_H2, 'W311_H3':W311_H3, 'W311d_Z1':W311d_Z1, 'W311d_Z2':W311d_Z2}
    
    return render(request, 'iot/index.html', context)

def transfer(request):
    return render(request, 'iot/transfer.html')

def welcome(request):
    return render(request, 'iot/welcome.html')