from geopy.distance import vincenty
from geopy.geocoders import Nominatim


def distance(a, b):
    geolocator = Nominatim()

    locate_a = geolocator.geocode(a)
    latlong_a = (locate_a.latitude, locate_a.longitude)
    locate_b = geolocator.geocode(b)
    latlong_b = (locate_b.latitude, locate_b.longitude)
    print(latlong_a)
    print(latlong_b)

    distance = vincenty(latlong_a, latlong_b).miles
    print(distance)


distance("Boston, MA", 'Washington, DC')
