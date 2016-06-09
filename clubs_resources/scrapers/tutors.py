import datetime
import os, sys, random, requests, re, json, io
from bs4 import BeautifulSoup
import tutorGCal

# Commented out because tutoring site is down
# url = "http://tutoring.csc.calpoly.edu/tutors.html"
# myRequest = requests.get(url)
# tutorSoup = BeautifulSoup(myRequest.text,"html.parser")
# Instead, use local copy of html file:
local_html = open("tutoring_csc_calpoly_edu_#tutors.html", 'r')
tutorSoup = BeautifulSoup(local_html.read(), "html.parser")

data_output_file = "../data/" + __file__.replace(".py", ".json")

def merge_calendar_info(tutors_dict):
   cal_info = tutorGCal.run()
   now = datetime.datetime.now()
   today_date = now.strftime('%Y-%m-%d')

   # assumes that the cal_info actually has the next seven days in it as well
   num_days_to_get = 7
   for date in cal_info:
      if today_date > date:
         print("ERROR: not enough info in calendar to get next seven days.")
         break
      if num_days_to_get == 0:
         break
      num_days_to_get -= 1

      day_of_week = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%A')
      scheduled_tutors = re.split(', | and | & ', cal_info[date]["tutors"])
      times = cal_info[date]["start"] + "-" + cal_info[date]["end"]
      for scheduled_tutor in scheduled_tutors:
         if scheduled_tutor in tutors_dict:
            tutors_dict[scheduled_tutor]["times"] = times
            if "days" in tutors_dict[scheduled_tutor]:
               tutors_dict[scheduled_tutor]["days"] += ", " + day_of_week
            else:
               tutors_dict[scheduled_tutor]["days"] = day_of_week
      

def main():
   f = open(data_output_file, 'w')

   tutors = {}
   for h2 in tutorSoup.find_all('h2'):
      nameList = h2.string.split()
      name = nameList[0] + " " + nameList[1]
      description = ""
      for string in h2.find_next('p').stripped_strings:
         description += string
      tutors[name] = {"description" : description.replace('\n', '')}

   #print("before: " + str(tutors))
   merge_calendar_info(tutors)
   #print("after: " + str(tutors))

   json.JSONEncoder().encode(tutors)
   json.dump(tutors, f)

if __name__ == "__main__":
   main()
