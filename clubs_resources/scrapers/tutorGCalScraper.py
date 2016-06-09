import httplib2, collections, json

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from datetime import datetime


# returns the dictionary
def run():
   
    http = httplib2.Http()

    service = build(serviceName='calendar', version='v3', http=http,
           developerKey='AIzaSyBNlYH01_9Hc5S1J9vuFmu2nUqBZJNAXxs')

    events = service.events().list(calendarId='uqokuji5ise4d2rutdost9k1j8@group.calendar.google.com').execute()
    tutorDict = {}
    #fp = open('../data/tutorGCal.json', 'w')

    for val in events.values():
        for v in val:
            for stuff in v:
                if (type(stuff) is str):
                    if(len(stuff.strip()) == 1 or stuff.strip() == ''):
                        continue
                    else:
                        if 'summary' in v.keys() and 'start' in v.keys() and 'end' in v.keys():
                            if 'dateTime' in v['start'] and 'dateTime' in v['end']:
                                date = v['start']['dateTime'].split('T')
                                date1 = date[0]
                                time = date[1].split('-')
                                time1 = time[0]
                                hms = time1.split(":")
                                setTime = 'AM'
                                hour = int(hms[0])
                                if hour > 12:
                                    hour -= 12
                                    setTime = 'PM'
                                startTime = str(hour) + ":" + hms[1] + setTime

                                date = v['end']['dateTime'].split('T')
                                date1 = date[0]
                                time = date[1].split('-')
                                time1 = time[0]
                                hms = time1.split(":")
                                setTime = 'AM'
                                hour = int(hms[0])
                                if hour > 12:
                                    hour -= 12
                                    setTime = 'PM'
                                endTime = str(hour) + ":" + hms[1] + setTime

                                tutor = v['summary'].split(':')
                                tutors = tutor[-1].strip()

                                tutorDict[date1] ={'tutors' : tutors, 'start' : startTime,
                                            'end' : endTime}

    od = collections.OrderedDict(sorted(tutorDict.items()))
    #json.JSONEncoder().encode(od)
    #json.dump(od, fp)

    return od

if __name__ == "__main__":
    print(run())
