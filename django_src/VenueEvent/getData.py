from .models import VenueEvent
import json
import pandas as pd

#Reset table
VenueEvent.objects.all().delete()

print('Reading data from Excel')
df = pd.read_excel('Venue_Event.xlsx', skiprows=1)

for i in range(df.shape[0]):
    data = df.iloc[i]
    event = VenueEvent(venue=data['Venue'], date=data['Date'], timeStart=data['Time start'], timeEnd=data['Time end'], event=data['Event'], instructor=data['Instructor'])
    event.save()

print('Finishing reading data from Excel')