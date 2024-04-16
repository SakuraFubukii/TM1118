from django.shortcuts import render
from .models import Event,tm1118_log

def index(request):
    events = tm1118_log.objects.all()[::50]
    W311a = tm1118_log.objects.filter(loc = 'W311a')[::50]
    W311b = tm1118_log.objects.filter(loc = 'W311b')[::50]
    W311_H1 = tm1118_log.objects.filter(loc = 'W311-H1')[::50]
    W311_H2 = tm1118_log.objects.filter(loc = 'W311-H2')[::50]
    W311_H3 = tm1118_log.objects.filter(loc = 'W311-H3')[::50]
    W311d_Z1 = tm1118_log.objects.filter(loc = 'W311d-Z1')[::50]
    W311d_Z2 = tm1118_log.objects.filter(loc = 'W311d-Z2')[::50]
    context = {'events':events, 'W311a':W311a, 'W311b':W311b, 'W311_H1':W311_H1, \
               'W311_H2':W311_H2, 'W311_H3':W311_H3, 'W311d_Z1':W311d_Z1, 'W311d_Z2':W311d_Z2}
    
    return render(request, 'iot/index.html', context)

def transfer(request):
    return render(request, 'iot/transfer.html')

def welcome(request):
    return render(request, 'iot/welcome.html')