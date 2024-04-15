from django.http import request
from django.shortcuts import render, redirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg
from datetime import datetime
from .models import VenueEvent
from . import getData
import datetime
import json

@csrf_exempt
def upload_excel(req):
    VenueEvents = VenueEvent.objects.all()
    ctx = {'VenueEvents': VenueEvents}
    if req.method == 'POST':
        postData = json.dumps(req.POST)
        try:
            startdate = req.POST["startdate"]
            starttime = req.POST["starttime"]
            enddate = req.POST["enddate"]
            endtime = req.POST["endtime"]
            print(startdate)
            print(enddate)
            VenueEvents = VenueEvent.objects.filter(date__gte=startdate, date__lte=enddate).order_by("-date")
            ctx = {'VenueEvents': VenueEvents}
            return render(req, 'Venue/upload.html', ctx)
        except Exception as e:
            print(e)
            return render(req, 'Venue/upload.html', ctx)

    else:
        VenueEvents = VenueEvent.objects.all()
        ctx = {'VenueEvents': VenueEvents}
        return render(req, 'Venue/upload.html', ctx)