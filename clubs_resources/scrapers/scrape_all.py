# Takes all the json files in the data directory and merges them into one dictionary,
# using their filenames (excluding '.json') as the key and their content as the value.

import os, json, sys
#from scrapers import *


# IMPORTANT VARIABLES HERE
path_to_data = "../data/" 
non_data_files = ["id_to_clubVariations.json", "variables_to_values.json"] #files to ignore that aren't data files, but are in data/


def get_scraped(scraper_scripts):
   json_files = [f[:-3] + ".json" for f in scraper_scripts if f not in non_data_files]
   big_dict = {}
   for json_file in json_files:
      f = open(path_to_data + json_file, 'r')
      big_dict[json_file[:-5]] = json.load(f)
      f.close()

   return big_dict


def run_scrapers():

   scraper_scripts = [pyfile for pyfile in os.listdir('.') if pyfile[-3:] == '.py' and pyfile != __file__ and pyfile != "__init__.py"]# <--- this path will need to be changed if file structure is changed
   #for scraper_script in scraper_scripts:
      #os.system("python3 " + scraper_script)
   
   big_dict = get_scraped(scraper_scripts)

   return big_dict


def get_all_data():
   return run_scrapers()


def main():
   print(run_scrapers())


if __name__ == '__main__':
   main()
