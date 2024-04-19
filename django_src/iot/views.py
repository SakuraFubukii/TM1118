from django.shortcuts import render
from .models import Event
from .models import Alert
from django.http import JsonResponse
from datetime import datetime, timedelta
#from . import iot_mqtt

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

def alert(request):
    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')
    if startdate and enddate:
        start_datetime = datetime.strptime(startdate, '%Y-%m-%d')
        end_datetime = datetime.strptime(enddate, '%Y-%m-%d') + timedelta(days=1)
        events = Alert.objects.filter(time__range=[start_datetime, end_datetime]).order_by('-time')
    else:
        events = Alert.objects.all().order_by('-time')
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data = []
        for event in events:
            data.append({
                'node_id': event.node_id,
                'loc': event.loc,
                'temp': event.temp,
                'hum': event.hum,
                'light': event.light,
                'snd': event.snd,
                'time': event.time.strftime('%Y-%m-%d %H:%M:%S')
            })
        return JsonResponse(data, safe=False)
    context = {'events': events}
    return render(request, 'iot/alert.html', context)