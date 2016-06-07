
import os, sys, random, requests, re, json, io
from bs4 import BeautifulSoup

url = "http://tutoring.csc.calpoly.edu/tutors.html"
myRequest = requests.get(url)
tutorSoup = BeautifulSoup(myRequest.text,"html.parser")

data_output_file = "../data/" + __file__.replace(".py", ".json")

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
	json.JSONEncoder().encode(tutors)
	json.dump(tutors, f)

if __name__ == "__main__":
    main()
