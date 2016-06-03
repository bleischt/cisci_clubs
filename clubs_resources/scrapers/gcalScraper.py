import sys, os, requests
from calendar_parser import CalendarParser


xml_feed = "https://calendar.google.com/calendar/embed?src=uqokuji5ise4d2rutdost9k1j8@group.calendar.google.com&ctz=America/Los_Angeles"


def main():
   cal = CalendarParser(xml_url=xml_feed)
   for event in cal.parse_calendar():
      print(event["name"])

if __name__ == "__main__":
   main()

