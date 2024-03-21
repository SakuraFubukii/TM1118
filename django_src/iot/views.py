from django.shortcuts import render
from .models import Event

def index(request):
    events = Event.objects.all()
    W311a = Event.objects.filter(loc = 'W311a')
    W311b = Event.objects.filter(loc = 'W311b')
    W311_H1 = Event.objects.filter(loc = 'W311-H1')
    W311_H2 = Event.objects.filter(loc = 'W311-H2')
    W311_H3 = Event.objects.filter(loc = 'W311-H3')
    W311d_Z1 = Event.objects.filter(loc = 'W311d-Z1')
    W311d_Z2 = Event.objects.filter(loc = 'W311d-Z2')
    context = {'events':events, 'W311a':W311a, 'W311b':W311b, 'W311_H1':W311_H1, \
               'W311_H2':W311_H2, 'W311_H3':W311_H3, 'W311d_Z1':W311d_Z1, 'W311d_Z2':W311d_Z2}
    
    return render(request, 'iot/index.html', context)