import os, sys, random, requests, re, json, io
from bs4 import BeautifulSoup
import wishGCal


url = "http://www.calpoly.edu/~wish/pages/officers.html"
myRequest = requests.get(url)
soup = BeautifulSoup(myRequest.text,"html.parser")

data_output_file =  "../data/" + __file__.replace(".py", ".json")

def main():
    tempf = open(data_output_file, 'w')

    wishDict = {}
    wishDict['officers'] = {}

    for h3 in soup.find_all("h3"):
        strings = []
        for string in h3.stripped_strings:
            strings.append(string)
        wishDict['officers'][strings[0]] = strings[1]

    wishDict['event_list'] = wishGCal.run()

    json.JSONEncoder().encode(wishDict)
    json.dump(wishDict, tempf)

if __name__ == "__main__":
    main()
