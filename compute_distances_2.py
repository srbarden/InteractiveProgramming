"""  Data Visualization Sarah Barden and Alisha Pegan
 Takes bing search data collected from news sources about Hillary and
  Michelle's travels and calculates additional data.
 New data include:
  1) shorten timestamp of the event to just include month, date, and year
  2) distance from their location and Washington D.C., where we assume is their
  home.
  The data collected ranges from the 1990s to 2017.
"""

# necessary libraries for calculating the locations and distances
import json
import datetime
from geopy.distance import vincenty
from geopy.geocoders import Nominatim

# ------------ LOAD DATA MINING --------------------
# opens json files with the stored data.
# The json files have a list of lists of dictionaries.
# The main list contains a list for each phrase that we searched.
# Each dicitonary within that list represents an article,
with open('michelle_data2.json', 'r') as json_data:
    michelle_news = json.load(json_data)

with open('hillary_data2.json', 'r') as json_data:
    hillary_news = json.load(json_data)


# ------------------ Add Distance and Shorter Date Dictionary--------------
# adds a new key called shortdate for every article
# adds a new key called distance for every article to calculate its geolocation

def shorter_date(news_articles):
    '''Shortens the existing publishing date to just include the month, day,
    and year. Adds it as key.

    no doctest for function: dictionaries are not ordered, and
     fail since the dictionary may return key in differnt order every time

    # >>> shorter_date([[{'date_pub': '2015-08-27T10:43:15'}]])
    # [[{'shortdate': '2015-08-27', 'date_pub': '2015-08-27T10:43:15'}]]

    # >>> shorter_date([[{'date_pub': '2011-01-24'}]])
    # [[{'shortdate': '2011-01-24', 'date_pub': '2011-01-24'}]]
    '''
    for phrase in news_articles:
        for article in phrase:
            fulldate = article['date_pub']  # gets the date publishded
            article['shortdate'] = fulldate[0:10]
    return news_articles


# get the updated data structure from shorter_date
mich = shorter_date(michelle_news)
hills = shorter_date(hillary_news)


def distance(news_articles):
    '''
    Computes distance from the location in each article to DC
    No doctests because dictionaries are not ordered
    '''
    geolocator = Nominatim()
    dc = geolocator.geocode('Washington, DC', timeout=200)
    latlong_dc = (dc.latitude, dc.longitude)
    for phrase in news_articles:
        for article in phrase:
            a = geolocator.geocode(article['location'], timeout=200)
            if a is None:
                a = dc
            latlong_a = (a.latitude, a.longitude)
            distance = vincenty(latlong_a, latlong_dc).miles
            article['distance'] = distance
            # print(article)
    return news_articles


mich_news = distance(mich)
hills_news = distance(hills)

# store data in json file
with open('michelle_locations.json', 'w') as outfile:
    json.dump(mich_news, outfile)

with open('hillary_locations.json', 'w') as outfile:
    json.dump(hills_news, outfile)
