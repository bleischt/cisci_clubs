
import os, sys, random, requests, re, json, io
from bs4 import BeautifulSoup

url = "http://tutoring.csc.calpoly.edu/home.html"
myRequest = requests.get(url)
tutorSoup = BeautifulSoup(myRequest.text,"html.parser")

data_output_file = "../data/" + __file__.replace(".py", ".json")

def main():
	f = open(data_output_file, 'w')
	tutoring = {}
	p = tutorSoup.find('p')
	pstring = p.string.replace('\n', '')
	pstringList = pstring.split('.')
	courses = re.split('CSC/CPE', pstringList[1])[1] + ','
	courses += re.split('including', pstringList[2])[1]
	tutoring['courses'] = courses
	p = p.find_next('p')
	p = p.find_next('p')
	p = p.find_next('p')
	lastParList = []
	for s in p.strings:
		lastParList.append(s)
	tutoring['building'] = re.search('([0-9]*)-([0-9]*)', lastParList[0]).group(1)
	tutoring['room'] = re.search('([0-9]*)-([0-9]*)', lastParList[0]).group(2)
	tutoring['startTime'] = re.search('([0-9])-([0-9])',lastParList[1]).group(1)
	tutoring['endTime'] = re.search('([0-9])-([0-9])',lastParList[1]).group(2)
	tutoring['startDay'] = 'Sunday'
	tutoring['endDay'] = 'Thursday'
	
	url = "http://tutoring.csc.calpoly.edu/contact_us.html"

	myRequest = requests.get(url)

	contactSoup = BeautifulSoup(myRequest.text,"html.parser")

	p = contactSoup.find('p')
	pstringList = re.split('lead tutor,', p.string)
	pstring = pstringList[1].replace('\n', '')
	pstringList = re.split(', at', pstring)
	tutoring['lead_tutor'] = pstringList[0]
	tutoring['contact_email'] = pstringList[1]

	json.JSONEncoder().encode(tutoring)
	json.dump(tutoring, f)
	
if __name__ == "__main__":
    main()
