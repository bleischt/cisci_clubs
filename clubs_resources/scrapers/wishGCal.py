
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

    return events

if __name__ == "__main__":
    run()

