import os, sys, ast, random, requests, re, json, io
from bs4 import BeautifulSoup


def get_officers():
    url = "http://calpolyieee.org/officers/"
    myRequest = requests.get(url)
    soup = BeautifulSoup(myRequest.text,"html.parser")

    tempf = open('temp_ieee_officers.json', 'w')

    ieee_officers = {}

    scripts = soup.find_all("script")
    for script in scripts:
       if "officer" in str(script.contents):
          match = re.search(".*(\[{.*}\]).*", str(script.contents))
          if match is not None:
             tempf.write(match.group(1))
          break
    tempf.close()

    tempf = open('temp_ieee_officers.json', 'r')
    #ieee_officers = ast.literal_eval(match.group(1)) <-- stupid ast didn't work! >:(
    ieee_officers = json.load(tempf)
    os.remove("temp_ieee_officers.json")
    
    return ieee_officers



def main():
    
    ieee_officers = get_officers()

    outfile = open('../data/ieee_officers.json', 'w')
    json.JSONEncoder().encode(ieee_officers)
    json.dump(ieee_officers, outfile)


if __name__ == "__main__":
    main()
