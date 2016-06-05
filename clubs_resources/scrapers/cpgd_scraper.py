import urllib.request as request
import bs4, json

cpgd_feed_url = 'http://cpgd.org/index.php/feed/'


def get_cpgd_event_data():
    with request.urlopen(cpgd_feed_url) as response_object:
        response_data = response_object.read()
        soup = bs4.BeautifulSoup(response_data, "html.parser")

        return get_cpgd_event_data_from_soup(soup)


def get_cpgd_event_data_from_soup(soup):
    # Get the most recent event posted in the feed.
    events = []

    latest_news_items = soup.find_all('item')
    for news_item in latest_news_items:
        event = {}

        news_item_title = news_item.find('title')
        if news_item_title != None:
            event['name'] = ' '.join(news_item_title.stripped_strings)

        news_item_description = news_item.find('description')
        if news_item_description != None:
            event['description'] = ' '.join(news_item_description.stripped_strings)

        events.append(event)
    
    return events


def main():
    events = get_cpgd_event_data()
    fp = open('../data/cpgd_data.json', 'w')
    json.dump({'club_events_data': events}, fp)


if __name__ == "__main__":
    main()
