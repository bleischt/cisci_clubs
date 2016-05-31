# This Python script gets the club data from the asi page
# (at http://www.asi.calpoly.edu/university_union/club_services).

import urllib.request as request
import bs4

#asi_clubs_url = "http://www.asi.calpoly.edu/university_union/club_services"
# It's actually here:
asi_clubs_url = "http://www.asi.calpoly.edu/club_directories/listing_bs/"


def get_asi_club_data():
    with request.urlopen(asi_clubs_url) as response_object:
        response_data = response_object.read()
        soup = bs4.BeautifulSoup(response_data, "html.parser")

        return get_club_data_from_soup(soup)

def get_club_data_from_soup(soup):
    data = []
    for club_record in soup.find_all("li", "club_list"):
        data.append(get_club_record_data(club_record))
    return data

def get_club_record_data(club_record):
    club_data = {}

    club_data["title"] = get_club_title(club_record)

    club_detail_pairs = generate_club_detail_pairs(club_record)

    for (detail_title, detail) in club_detail_pairs:
        club_data[detail_title] = detail

    return club_data
    
def get_club_title(club_record):
    return next(club_record.find("a", alt="Club Details").stripped_strings)

def generate_club_detail_pairs(club_record):
    detail_titles = club_record.find_all("span", "club_details_title")
    details = club_record.find_all("span", "club_details")

    # If detail_titles and details don't have the same length,
    # that will be a problem. Just use as many pairs as there are.
    for i in range(min(len(detail_titles), len(details))):
        yield (str(detail_titles[i].string), str(details[i].string))

data = get_asi_club_data()
print(data)
