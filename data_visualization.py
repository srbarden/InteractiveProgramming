import json
import indicoio
from indico_knock import Indico_KEY

from geopy.distance import vincenty
from geopy.geocoders import Nominatim

# ------------ DATA MINING --------------------
with open('michelle_data.json', 'r') as json_data:
    michelle_news = json.load(json_data)

with open('hillary_data.json', 'r') as json_data:
    hillary_news = json.load(json_data)

print(len(michelle_news))
print(len(hillary_news))

indicoio.config.api_key = Indico_KEY


# print(michelle_news[0][3]['description'])
# positive = [tweet for tweet in tweet_data if tweet['sentiment']['pos'] > 0]


michelle_places = []
# there are four main search_phrases
for search_phrases in michelle_news:
    # for each article in the results for each search phrase, checks if the
    # the title contains the phrase "Michelle Obama"
    for article in search_phrases:
        if 'Michelle Obama' in article['title']:
            # apply the indico place API to the title
            # if there are results, keep the article
            # print(article['title'])
            place = indicoio.places(article['title'])
            if len(place) > 0:
                temp_dic = {}
                temp_dic['title'] = article['title']
                temp_dic['location'] = place[0]['text']
                temp_dic['description'] = article['description']
                temp_dic['date_pub'] = article['date_pub']
                temp_dic['url'] = article['url']
                michelle_places.append(temp_dic)

print(len(michelle_places))

print(michelle_places)
# print(relevant[1]['description'])

# sort list to show greatest location with highest confidence to location with lowest
# sorted_locations = sorted(k, key=lambda k: k['confidence'], reverse=True)
# print(sorted_locations)
# j = indicoio.places("U.S. first lady Michelle Obama meets with the children ", threshold=0.01)
# print(j)
# print(j[0]['text'])
# print(dir(indicoio))


# --------------------- LOCATIONS into POINTS-----------------------
michelle_points = []
for dictionary in michelle_places:
    place = michelle_places[dictionary[location]]
    datetime = michelle_places[dictionary[date_pub]]
    date = datetime[0:10]
    michelle_points.append((date, place))

hillary_points = []
for dictionary in michelle_places:
    place = hillary_places[dictionary[location]]
    datetime = hillary_places[dictionary[date_pub]]
    date = datetime[0:10]
    hillary_points.append((date, place))

# -------------------- GEOCODER --------------------------------------
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

# -------------DIST B/T HILLARY AND MICHELLE---------------------

distance("Kensington Palace", 'Washington, DC')


# ------------------ DRAWING -------------------------------------

def make_figure():
    pygame.init()
    width = 1200
    height = 800
    mid = int(height/2)
    figure = pygame.display.set_mode((width, height))

    red = (200, 0, 0)
    green = (0, 200, 0)
    blue = (0, 0, 200)
    white = (255, 255, 255)
    black = (0, 0, 0)

    # maps hypothetical times and distance between three people
    distances12 = {1: 200, 2: 50, 3: 50, 4: 0, 5: 100, 6: 0}
    # distances23 = {1: 50, 2: 0, 3: 100, 4: 0, 5: 100, 6: 100}
    # distances31 = {1: 100, 2: 50, 3: 100, 4: 0, 5: 0, 6: 100}

    # this keeps the window open until you press the x
    done = False
    clock = pygame.time.Clock()
    while not done:
        clock.tick(10)  # 10 times per second through the loop
        for event in pygame.event.get():  # for an event
            if event.type == pygame.QUIT:  # if you click close
                done = True   # done to exit this loop

        figure.fill(white)  # supposed to make figure white
        pointlist1 = []
        pointlist2 = []
        meetings = []

# --------- DRAWING LINES AND POINTS--------------------------------
        for key in distances12:
            dist12 = distances12[key]
            dist23 = distances23[key]

            point1 = mid - 0.5*dist12
            point2 = mid + 0.5*dist12

            point1 = mid - 0.5*dist12  # calculates points for person 1
            point2 = mid + 0.5*dist12  # calculates points for person 2

            pointlist1.append((key*150, point1))
            pointlist2.append((key*150, point2))

        pygame.draw.lines(screen, red, False, pointlist1, 2)
        pygame.draw.lines(screen, green, False, pointlist2, 2)

            if dist12 == 0:
                meetings.append((key*150, mid))

        for point in meetings:
            pygame.draw.circle(figure, black, point, 10, 0)

        pygame.draw.lines(figure, red, False, pointlist1, 5)
        pygame.draw.lines(figure, green, False, pointlist2, 5)
    # -------------------- MOUSE EVENT ----------------------
        p = pygame.mouse.get_pos()
        for point in meetings:

        if p in meetings:
            figure.fill(black)

        pygame.display.update()

    mouse_loc = pygame.mouse.get_pos()
    if mouse_loc in pointlist1 or pointlist2:
        print('hi')
    # if event.type == pygame.MOUSEBUTTONDOWN:


make_figure()
