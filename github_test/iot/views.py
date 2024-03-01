from django.shortcuts import render
from .models import Event

def index(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request, 'iot/index.html', context)

def W311a(request):
    W311a = Event.objects.filter(loc = 'W311a')
    context = {'W311a':W311a}
    return render(request, 'iot/sensor/W311a.html', context)

def W311b(request):
    W311b = Event.objects.filter(loc = 'W311b')
    context = {'W311b':W311b}
    return render(request, 'iot/sensor/W311b.html', context)
    
def W311_H1(request):
    W311_H1 = Event.objects.filter(loc = 'W311-H1')
    context = {'W311_H1':W311_H1}
    return render(request, 'iot/sensor/W311-H1.html', context)

def W311_H2(request):
    W311_H2 = Event.objects.filter(loc = 'W311-H2')
    context = {'W311_H2':W311_H2}
    return render(request, 'iot/sensor/W311-H2.html', context)

def W311_H3(request):
    W311_H3 = Event.objects.filter(loc = 'W311-H3')
    context = {'W311_H3':W311_H3}
    return render(request, 'iot/sensor/W311-H3.html', context)

def W311d_Z1(request):
    W311d_Z1 = Event.objects.filter(loc = 'W311d-Z1')
    context = {'W311d_Z1':W311d_Z1}
    return render(request, 'iot/sensor/W311d-Z1.html', context)

def W311d_Z2(request):
    W311d_Z2 = Event.objects.filter(loc = 'W311d-Z2')
    context = {'W311d_Z2':W311d_Z2}
    return render(request, 'iot/sensor/W311d-Z2.html', context)