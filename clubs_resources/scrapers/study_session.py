import os, sys, random, requests, json
from bs4 import BeautifulSoup

data_output_file = "../data/" + __file__.replace(".py", ".json")

def main():

        fp = open(data_output_file, 'w')

        url = "http://sas.calpoly.edu/studysession/"
        myRequest = requests.get(url)
        soup = BeautifulSoup(myRequest.text,"html.parser")

        studyDict = {}
        table = soup.find_all('div', {'id':'mainLeftFull'})
        for t in table:

            info = t.find_all('p')
            info1 = [ele.text.strip() for ele in info]
            studyDict['description'] = info1[0]

            rows = t.find_all('tr')

            for row in rows:
                    name = row.find_all('th')
                    names = [ele.text.strip() for ele in name]

                    value = row.find_all('td')
                    values = [ele.text.strip() for ele in value]

                    names = names[0][:-1]

                    values = values[0]
                    values = values.replace('\r','')
                    values = values.replace('  ', '')
                    names = names.lower()
                    names = names.replace(' ', '_')
                    studyDict[names] = values

        json.JSONEncoder().encode(studyDict)
        json.dump(studyDict, fp)

if __name__ == "__main__":
        main()

