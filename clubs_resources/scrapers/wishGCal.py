
import httplib2, collections, json

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from datetime import datetime

def run():
    http = httplib2.Http()

    service = build(serviceName='calendar', version='v3', http=http,
           developerKey='AIzaSyBNlYH01_9Hc5S1J9vuFmu2nUqBZJNAXxs')

    events = service.events().list(calendarId='wishcalpoly@gmail.com').execute()

    eventDict = {}

    for k in events['items']:
        eventDict[k['summary']] = {}
        if 'location' in k:
            eventDict[k['summary']]['event_location'] = k['location']
        else:
            eventDict[k['summary']]['event_location'] = ''
        if 'dateTime' in k['start']:
            eventDict[k['summary']]['event_start_time'] = k['start']['dateTime']
        else:
            eventDict[k['summary']]['event_start_time'] = ''
        if 'dateTime' in k['end']:
            eventDict[k['summary']]['event_end_time'] = k['end']['dateTime']
        else:
            eventDict[k['summary']]['event_end_time'] = ''
            
    return eventDict

if __name__ == "__main__":
    print(run())

