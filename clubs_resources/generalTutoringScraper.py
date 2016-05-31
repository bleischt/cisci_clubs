
import os, sys, random, requests, re, json, io
from bs4 import BeautifulSoup

url = "http://tutoring.csc.calpoly.edu/home.html"

myRequest = requests.get(url)

tutorSoup = BeautifulSoup(myRequest.text,"html.parser")

def main():
	#f = open('general_tutoring_json.txt', 'w')
	tutoring = {}
	p = tutorSoup.find('p')
	pstring = p.string.replace('\n', '')
	pstringList = pstring.split('.')
	courses = re.split('CSC/CPE', pstringList[1])[1] + ','
	courses += re.split('including', pstringList[2])[1]
	tutoring['courses': courses]
	
	
	
if __name__ == "__main__":
    main()
