#! /usr/bin/env python

from bs4 import BeautifulSoup
import re, json, requests


history_url = "http://cplug.org/about/a-brief-history-of-cplug/"
contact_url = "http://cplug.org/contact/"
years_pos_people = {} 
years = {}
data_output_file = "../data/" + __file__.replace(".py", ".json")

# Takes in a string like "2003-2005" and returns a list
# like [2003, 2004, 2005]
def yr_range_to_list(yr_range):
    begin = int(yr_range.split('-')[0])
    end = int(yr_range.split('-')[1])
    yr_list = []
    yr_list.append(begin)
    cur = begin
    while (cur < end):
        cur += 1
        yr_list.append(cur)
    yr_list.append(end)

    return yr_list

def get_history():
    myRequest = requests.get(history_url)
    soup = BeautifulSoup(myRequest.text, "html.parser")
    cur_p = soup.find('p')
     
    cur_p = cur_p.find_next('p')
    while (cur_p != None):
       years = cur_p.contents[0]
       match = re.search('^(\d+-\d+)', years)
       if (match == None):
          print("ERROR: regex match on years somehow got None")
       else:
          years = match.group(1)
        
       pos_person_dict = {}
       cur_p = cur_p.find_next('ul')
       pre_people = list(filter(lambda a: a != '\n', cur_p.contents))
       for pos_person in pre_people:
          pos_person = pos_person.string
          pos_person = pos_person.replace('<li>', '')
          pos_person = pos_person.replace('</li>', '')
          splitted = pos_person.split(':')
          if (len(splitted) == 2):
             pos_person_dict[splitted[0].lower().strip()] = splitted[1].lower().strip()

       if (len(pos_person_dict) > 0):
          for yr in yr_range_to_list(years):
              years_pos_people[yr] = pos_person_dict
        
       cur_p = cur_p.find_next('p')
       return years_pos_people


def get_current_officers():
    myRequest = requests.get(contact_url)
    soup = BeautifulSoup(myRequest.text, "html.parser")
    cur_p = soup.find('section', {'class': 'post-content'})
    cur_p = cur_p.find('ul', {'id': 'officers'})
    
    officers = {}
    cur_p = cur_p.find('li')
    list_p = cur_p
    while list_p:
       pos = list_p.find('h4').contents[0]
       description = list_p.find('img').find('p').contents[0]
       name = description.split()[0]
       officers[name] = pos

       cur_p = cur_p.find_next('li')
       list_p = cur_p

    return officers
    
   
def main():
    main_cplug = {}
    main_cplug['officers_history'] = get_history()
    main_cplug['officers'] = get_current_officers()

    outfile = open(data_output_file, 'w')
    json.JSONEncoder().encode(main_cplug)
    json.dump(main_cplug, outfile)

if __name__ == "__main__":
    main()
