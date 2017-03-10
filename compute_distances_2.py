"""  Data Visualization Sarah Barden and Alisha Pegan
 Takes data collected from news sources about Hillary and Michelle's
 travels and creates a figure that shows that distance between them
 over time.  The data collected ranges from the 1990s to 2017.
"""
import json
import datetime
from datetime import date
from time import sleep
from geopy.distance import vincenty
from geopy.geocoders import Nominatim

import numpy as np
import pandas as pd

# ------------ DATA MINING --------------------
# opens json files with the stored data.
# The json files have a list of lists of dictionaries.
# The main list contains a list for each phrase that we searched.
# Each dicitonary within that list represents an article,
with open('michelle_data2.json', 'r') as json_data:
    michelle_news = json.load(json_data)

with open('hillary_data2.json', 'r') as json_data:
    hillary_news = json.load(json_data)

# print(len(michelle_news))
# print(len(hillary_news))


# --------------------- ARTICLE INTO (TIME, PLACE)-----------------------
# Gets location names for Michelle and Hillary from all the data articles
# Creates dictionary for each person with dates as keys, locations as values.

def compute_distances(newsource):
    # Creates dictionary for Michelle's locations
    for phrase in newsource:
        for article in phrase:
            # print(article)
            fulldate = article['date_pub']  # gets the date publishded
            article.update({'shortdate': fulldate[0:10]})
            print(article)

compute_distances(michelle_news)
    # Creaets a dictionary for Hillary's locations
    # hillary_places = {}
    # for phrase in hillary_news:
    #     for article in phrase:
    #         place = article['location']
    #         fulldate = article['date_pub']
    #         shortdate = fulldate[0:10]
    #         hillary_places[shortdate] = place

    # Supposed to cut out dates before 2008. Not sure if it works
    # keys = [k for k, v in michelle_places.items() if int(k[0:3]) < 2008]
    # for x in keys:
    #     del michelle_places[x]

    # print(michelle_points)
    # print(hillary_points)

    # ------------------- FILLING IN MISSING POINTS ----------------------
    # Assume that when not traveling, Hillary and Michelle were in DC
    # For any date that is not in hillary_points or michelle_points, add that
    # date and 'Washington, DC'

    # Iterate through each date, so need a start and end date
#     startdate = datetime.date(1990, 1, 1)
#     enddate = datetime.date(2017, 3, 6)
#     day = datetime.timedelta(days=1)  # timedelta object, represents one days
#
#     date = startdate  # date is the iterator
#     while date < enddate:
#         date_pretty = date.isoformat()  # datetime object to 'yyyy-mm-dd'
#         if date_pretty not in michelle_places:
#             michelle_places[date_pretty] = 'Washington, DC'
#         if date_pretty not in hillary_places:
#             hillary_places[date_pretty] = 'Washington, DC'
#         date += day
#
#     # print(hillary_points['2016-05-13'])  # Brooklyn, test for known location
#
#     # hillary_points = {'1-1-17': 'Los Angeles', ...}
#     locs = [michelle_places, hillary_places]
#
#     # -------------------- GEOCODER -------------------------------------
#     """
#     This distance function takes two strings of location names and
#     returns the distance bewtween them
#     """
#
#     def distance(loc):
#         # computes distance of loc from DC
#         geolocator = Nominatim()
#         dc = geolocator.geocode('Washington, DC', timeout=50)
#         latlong_dc = (dc.latitude, dc.longitude)
#         a = geolocator.geocode(loc, timeout=50)
#         if a is None:
#             a = dc
#         latlong_a = (a.latitude, a.longitude)
#
#         distance = vincenty(latlong_a, latlong_dc).miles
#         sleep(1)
#         return distance
#
#         # except GeocoderTimedOut:
#         #    print("timed out")
#
#     # -------------DIST B/T PERSON and DC---------------------
#
#     places = locs[0]   # will loop twice: for Michelle and Hillary
#     # print(places)
#     michelle_dist = []
#     for key in places:
#         # print(places[key])
#         dist_calc = distance(places[key])
#         michelle_dist.append(dist_calc)
#     # print(michelle_dist)
#
# # -----------------Dataset------------------------------
#
#     michelle_locations = pd.Series(places, name='Location')
#     # michelle_distance = pd.Series(places, name='Distance')
#     # michelle_description = pd.Series(places, name='Description')
#     michelle_locations.index.name = 'Date'
#     michelle_locations.reset_index()
#     data = pd.DataFrame(michelle_locations)
#     print(data)
#     return data
#
# # print(michelle_news)
# compute_distances()
