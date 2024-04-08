from django.shortcuts import render
import pandas as pd
from datetime import datetime
from .models import Event
import datetime

def upload_excel(request):
    df = pd.read_excel("Venue_Event.xlsx")
    events = []
    for x in range(1, len(df)):
        event = Event()
        event.venue = df.loc[x, df.columns[0]].upper()
        event_date =  datetime.datetime.strptime(str(df.loc[x, df.columns[1]]), "%Y-%m-%d %H:%M:%S")
        event.time_start = datetime.datetime.combine(event_date, df.loc[x, df.columns[2]])
        event.time_end = datetime.datetime.combine(event_date, df.loc[x, df.columns[3]])
        event.event_name = df.loc[x, df.columns[4]]
        event.instructor = df.loc[x, df.columns[5]]
        event.save()
        events.append(event)
    context = {'events':events}
    return render(request, 'Venue/upload.html',context)