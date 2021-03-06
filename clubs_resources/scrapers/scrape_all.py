# Takes all the json files in the data directory and merges them into one dictionary,
# using their filenames (excluding '.json') as the key and their content as the value.

import os, json, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from variable_replace import standardize_club 

# IMPORTANT VARIABLES HERE
path_to_data = "../data/" 
ignore_files = [__file__, "__init__.py", "wishGCal.py", "tutorGCal.py"]
non_data_files = ["id_to_clubVariations.json", "variables_to_values.json"] #files to ignore that aren't data files, but are in data/
club_files = ["wish.json", "ieee.json", "swe.json", "cplug.json"] # ***** add new club files here to be added to the big club dict ******
id_to_variations = "../data/id_to_clubVariations.json"

# using data from club_files and general_club, makes one big club data dictionary
def make_club_dict(general_club_json_f):
   clubs_dict = json.load(general_club_json_f)
   
   for scraped_club in club_files:
      merged = False
      #os.system('pwd')
      f = open(path_to_data + scraped_club, 'r')
      new_data = json.load(f)
      std_scraped_club = standardize_club(scraped_club[:-5], id_to_variations)

      for club in clubs_dict.keys():
         if club == std_scraped_club:
            # add data to this dict
            #print("update '" + club + "' entry with: " + str(new_data))
            clubs_dict[club].update(new_data) # using update will override any duplicate keys
            merged = True
            break
      if not merged:
         #print("add '" + std_scraped_club + "' to the dictionary")
         clubs_dict[std_scraped_club] = new_data

   return clubs_dict

def get_scraped(scraper_scripts):
   json_files = [f[:-3] + ".json" for f in scraper_scripts if f not in non_data_files and f[:-3] + ".json" not in club_files]
   big_dict = {}
   for json_file in json_files:
      f = open(path_to_data + json_file, 'r')
      if json_file == "club_info.json":
         big_dict["club"] = make_club_dict(f)
      else:
         big_dict[json_file[:-5]] = json.load(f)
      f.close()

   return big_dict


def run_scrapers():
   
   scraper_scripts = [pyfile for pyfile in os.listdir('.') if pyfile[-3:] == '.py' and pyfile not in ignore_files]# <--- this path will need to be changed if file structure is changed

   for scraper_script in scraper_scripts:
      try:
         os.system("python3 " + scraper_script)
      except:
         print("ERROR: exception while running " + scraper_script)
   
   big_dict = get_scraped(scraper_scripts)

   return big_dict


def get_all_data():
   return run_scrapers()


def main():
   #print(run_scrapers())
   f = open ("../data/all_data.json", 'w')
   data = get_all_data()
   json.JSONEncoder().encode(data)
   json.dump(data, f)


if __name__ == '__main__':
   main()
