import os, sys, random, requests, re, json, io
from bs4 import BeautifulSoup

url = "https://swe.calpoly.edu/contact-us/"

myRequest = requests.get(url)

soup = BeautifulSoup(myRequest.text,"html.parser")

def main():
        f = open('../data/swe_info.json', 'w')
        swe = {}
        tables = soup.find_all('table')
        for table in tables:
            body = table.find_all('tbody')
            for b in body:
                rows = b.find_all('tr')
                for row in rows:
                    #print(row)
                    name = row.find_all('td')
                    names = [ele.text.strip() for ele in name]
                    if names[0] == '':
                        if names[1:][0] != '' and names[1:][2] != '':
                            swe[names[1:][0]] = names[1:][2]
                    else:
                        swe[names[0]] = names[1]

        json.JSONEncoder().encode(swe)
        json.dump(swe, f)

if __name__ == "__main__":
    main()