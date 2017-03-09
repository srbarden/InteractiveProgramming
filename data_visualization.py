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
# Creates a dictionary for each person with dates as keys and locations as values.

def compute_distances():

    # Creates dictionary for Michelle's locations
    michelle_points = {}
    for phrase in michelle_news:
        for article in phrase:
            # print(article)
            place = article['location']      # gets the locations name
            fulldate = article['date_pub']   # gets the date of publication
            date = fulldate[0:10]            # gets only the date and not the time
            michelle_points[date] = place

    # Creaets a dictionary for Hillary's locations
    hillary_points = {}
    for phrase in hillary_news:
        for article in phrase:
            place = article['location']
            fulldate = article['date_pub']
            date = fulldate[0:10]
            hillary_points[date] = place

    # Supposed to cut out dates before 2008. Not sure if it works
    keys = [k for k, v in michelle_points.items() if int(k[0:3]) < 2008]
    for x in keys:
        del michelle_points[x]

    # print(michelle_points)
    # print(hillary_points)

    # ------------------- FILLING IN MISSING POINTS ----------------------
    # Assume that when not traveling, Hillary and Michelle were in Washnigton, DC
    # For any date that is not in hillary_points or michelle_points, we add that
    # date and 'Washington, DC'

    # Iterate through each date, so need a start and end date
    startdate = datetime.date(1990, 1, 1)
    enddate = datetime.date(2017, 3, 6)
    day = datetime.timedelta(days=1)  # this is a timedelta object, represents one days

    date = startdate  # date is the iterator
    while date < enddate:
        date_pretty = date.isoformat() # turns datetime object into 'yyyy-mm-dd'
        if date_pretty not in michelle_points:
            michelle_points[date_pretty] = 'Washington, DC'
        if date_pretty not in hillary_points:
            hillary_points[date_pretty] = 'Washington, DC'
        date += day

    # print(hillary_points['2016-05-13'])  # Brooklyn, testing for known location

    # Craete a dictionary to hold the dates and both locations
    locations = {}
    for i in hillary_points:
        # print(hillary_points[i])
        locations[i] = [hillary_points[i], michelle_points[i]]


    # -------------------- GEOCODER -------------------------------------
    """
    This distance function takes two strings of location names and returns the distance b
    """

    def distance(a, b):
        geolocator = Nominatim()

        try:
            locate_a = geolocator.geocode(a, timeout=50)
        except GeocoderTimedOut:
            print("timed out")
        if locate_a is None:
            locate_a = geolocator.geocode('Washington, DC')
        latlong_a = (locate_a.latitude, locate_a.longitude)
        sleep(1)

        locate_b = geolocator.geocode(b, timeout=50)
        if locate_b is None:
            locate_b = 'Washington, DC'
        latlong_b = (locate_b.latitude, locate_b.longitude)

        distance = vincenty(latlong_a, latlong_b).miles
        return distance

    # -------------DIST B/T HILLARY AND MICHELLE---------------------
    distances = {}
    for i in locations:
        pair = locations[i]
        if pair[0] == pair[1]:
            pass
        else:
            d = distance(pair[0], pair[1])  # ru ndistance function between two locaitons
            distances[i] = d
            # print('not washington')
            sleep(1)

    return distances

    
compute_distances()
