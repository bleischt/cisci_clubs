# Takes all the json files in the data directory and merges them into one dictionary,
# using their filenames (excluding '.json') as the key and their content as the value.

import os, json, sys
from scrapers import *

def run_scrapers():

   scraper_scripts = [pyfile for pyfile in os.listdir('scrapers') if pyfile[-3:] == '.py']# <--- this path will need to be changed if file structure is changed
   print(scraper_scripts)

   return



def main():
   run_scrapers()
   return


if __name__ == '__main__':
   main()
