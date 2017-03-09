import json
import pygame
import datetime
from geopy.distance import vincenty
from geopy.geocoders import Nominatim

# ------------ DATA MINING --------------------
with open('michelle_data2.json', 'r') as json_data:
    michelle_news = json.load(json_data)

with open('hillary_data2.json', 'r') as json_data:
    hillary_news = json.load(json_data)

print(len(michelle_news))
print(len(hillary_news))


# --------------------- ARTICLE INTO (TIME, PLACE)-----------------------


michelle_points = {}
for phrase in michelle_news:
    for article in phrase:
        # print(article)
        place = article['location']
        fulldate = article['date_pub']
        date = fulldate[0:10]
        michelle_points[date] = place

# print(michelle_points)

hillary_points = {}
for phrase in hillary_news:
    for article in phrase:
        place = article['location']
        fulldate = article['date_pub']
        date = fulldate[0:10]
        hillary_points[date] = place
print(hillary_points)

# ------------------- FILLING IN MISSING POINTS ----------------------
# Assume that when not traveling Hillary and Michelle were at the White House.


def fillindates():
    startdate = datetime.date(2012, 1, 1)
    enddate = datetime.date(2016, 12, 1)
    day = datetime.timedelta(days=1)

    date = startdate
    while date <= enddate:
        if date not in michelle_points:
            date_pretty = date.isoformat()
            michelle_points[date_pretty] = 'Washington, DC'
        if date not in hillary_points:
            date_pretty = date.isoformat()
            hillary_points[date_pretty] = 'Washington, DC'
        date += day

    # michelle_points_sort = sorted(michelle_points, key=lambda x: x[0], reverse=False)
    # hillary_points_sort = sorted(hillary_points, key=lambda x: x[0], reverse=False)

    print(michelle_points)


# fillindates()


# -------------------- GEOCODER -------------------------------------
def distance(a, b):
    geolocator = Nominatim()

    locate_a = geolocator.geocode(a)
    latlong_a = (locate_a.latitude, locate_a.longitude)
    locate_b = geolocator.geocode(b)
    latlong_b = (locate_b.latitude, locate_b.longitude)
    print(latlong_a)
    print(latlong_b)

    distance = vincenty(latlong_a, latlong_b).miles
    return distance

# -------------DIST B/T HILLARY AND MICHELLE---------------------

distances = []


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

            point1 = mid - 0.5*dist12  # calculates points for person 1
            point2 = mid + 0.5*dist12  # calculates points for person 2

            pointlist1.append((key*150, point1))
            pointlist2.append((key*150, point2))

        pygame.draw.lines(figure, red, False, pointlist1, 2)
        pygame.draw.lines(figure, green, False, pointlist2, 2)

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

# --------------------- CLASSES------------------------


class TimeLine:
    '''
    Encodes the display state
    '''
    def __init__(self):
        pass


class Line:
    '''
    Encodes the state of the line in the display
    '''
    def __init__(self, color, height, width, x, y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y


class Meeting:
    '''
    Encodes the state the meeting point circles in the game
    '''
    def __init__(self, color, height, width, x, y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y


class PyGameWindowView:
    '''
    A view of the display rendered in a Pygame window
    '''
    def __init__(self, model, screen):
        pass


class PyGameMouseController:
    '''
    Encodes the mouse controller for it to show meeting point
    when mouse scrolls over it
    '''

if __name__ == '__main__':
    pygame.init()
    size = ()
