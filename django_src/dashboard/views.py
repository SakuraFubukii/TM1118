from django.http import request
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.db.models import Avg
from iot.models import Event

def index(req):
    return render(req, 'dashboard/index.html')

def dashboard(req):
    return render(req, 'dashboard/dashboard.html')

def test(req):
    events = Event.objects.values("loc").distinct()
    ctx = {'testdata': events}
    return render(req, 'dashboard/test.html', ctx)

def data_dashboard(req):
    events = Event.objects.all().order_by("-time")[:7]
    events = Event.objects.all().order_by("-time")[:7]

    for event in events:
        event.temp = int(event.temp)
        event.hum = int(event.hum)
        event.light = int(event.light)
        event.snd = int(event.snd)
    data = serializers.serialize('json', events)
    return JsonResponse(data, safe=False)

def graph_overview(req):
    ctx = {}
    return render(req, 'dashboard/showGraphByCat.html', ctx)

def data_test2(req):
    d = datetime.datetime.now().replace(second=0, microsecond=0) - \
        datetime.timedelta(minutes=2)

    events = Event.objects.filter(
        time__gte=d, time__lt=d + datetime.timedelta(minutes=1))
    print(events.aggregate(Avg('temp'))["temp__avg"])
    print(events.aggregate(Avg('hum'))["hum__avg"])
    print(events.aggregate(Avg('light'))["light__avg"])
    print(events.aggregate(Avg('snd'))["snd__avg"])
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)

def showB05(req):
    ctx = {}
    ctx['node_id'] = "B05"
    events = Event.objects.filter(
        node_id=ctx['node_id']).order_by("-time")
    ctx['events'] = events

    return render(req, 'dashboard/datashow.html', ctx)
    
def data_events(req):
    events = Event.objects.all().order_by("-time")[:10]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)

def location(req):
    ctx = {}
    return render(req, 'dashboard/showGraphByCat.html', ctx)

@csrf_exempt
def data_test1(req):
    ctx = {}
    if req.method == 'POST':

        postData = json.dumps(req.POST)
        try:
            events = Event.objects.filter(
                req.POS.node_loc).order_by("-time")[:10]

            eventsData = serializers.serialize('json', events)
            print(eventsData)
            if eventsData == []:
                print('err')
                raise Exception
            return JsonResponse(eventsData, safe=False)
            


        except:
            locList = ['W311-H1', 'W311-H2', 'W311-H3', 'W311A', 'W311B', 'W311D-Z1', 'W311D-Z2']
            events = {}
            for x in locList:
                events[x] = Event.objects.filter(x).order_by("-time")[:10]
                events[x]  = serializers.serialize('json', x)
           

            eventsData = json.dumps(events)
            print(eventsData)
            return JsonResponse(eventsData, safe=False)

        postData = json.dumps(req.POST)

        return JsonResponse(postData, safe=False)
        # return redirect('/blog/')

    else:

        return render(req, 'dashboard/datatest.html', ctx)


@csrf_exempt
def data_test(req):
    ctx = {}
    if req.method == 'POST':

        postData = json.dumps(req.POST)
        try:
            events = Event.objects.filter(
                node_loc=req.POST["node_loc"]).order_by("-time")[:10]

            eventsData = serializers.serialize('json', events)
            print(eventsData)
            if str(eventsData) == "[]":
                raise Exception
            return JsonResponse(eventsData, safe=False)
            

        except:
            locList = ['W311-H1', 'W311-H2', 'W311-H3', 'W311A', 'W311B', 'W311D-Z1', 'W311D-Z2']
            events = []
            for x in locList:
                
                event = Event.objects.filter(node_loc=x).order_by("-time")[:10]
                events.append(serializers.serialize('json', event))
           
           

            eventsData = json.dumps(events)

            return JsonResponse(eventsData, safe=False)

        postData = json.dumps(req.POST)

        return JsonResponse(postData, safe=False)
        # return redirect('/blog/')

    else:

        return render(req, 'dashboard/datatest.html', ctx)


def data_dashboardA01(req):
    events = Event.objects.filter(node_id='A01').order_by("-time")[:7]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)