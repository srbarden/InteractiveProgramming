"""  Data Visualization Sarah Barden and Alisha Pegan
 Takes data collected from news sources about Hillary and Michelle's
 travels and creates a figure that shows that distance between them
 over time.  The data collected ranges from the 1990s to 2017.
"""
import json
import pygame
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
# for i in hillary_points:
#     print(hillary_points[i])

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


print('done with distances')
# ------------------ DRAWING -------------------------------------


def make_figure():
    pygame.init()
    width = 1200
    height = 800
    mid = int(height/2)
    figure = pygame.display.set_mode((width, height))
    menu_font = pygame.font.Font(None, 12)

    red = (200, 0, 0)
    green = (0, 200, 0)
    blue = (0, 0, 200)
    white = (255, 255, 255)
    black = (0, 0, 0)

    # maps hypothetical times and distance between three people
    # distances12 = {1: 200, 2: 50, 3: 50, 4: 0, 5: 100, 6: 0}

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
        for key in distances:
            dist = 0.1*distances[key]  # scale down distances

            point1 = mid - 0.5*dist
            point2 = mid + 0.5*dist

            point1 = mid - 0.5*dist  # calculates points for person 1
            point2 = mid + 0.5*dist  # calculates points for person 2

            year = int(key[0:4])
            month = int(key[5:7])
            day = int(key[8:10])
            t = datetime.date(year, month, day)

            x = (t - datetime.date(1990, 1 ,1)).total_seconds()

            pointlist1.append((x/1000000, point1))
            pointlist2.append((x/1000000, point2))

        pointlist1.sort()
        pointlist2.sort()

        pygame.draw.lines(figure, blue, False, pointlist1, 2)
        pygame.draw.lines(figure, green, False, pointlist2, 2)


        if dist == 0:
            meetings.append((key, mid))

        for point in meetings:
            circle = pygame.draw.circle(figure, black, point, 10, 0)

        pygame.draw.lines(figure, red, False, pointlist1, 5)
        pygame.draw.lines(figure, green, False, pointlist2, 5)

# -------------------- MOUSE EVENT ----------------------
        p = pygame.mouse.get_pos()
        for point in meetings:
            if p in circle:
                figure.fill(black)

        pygame.display.update()

    mouse_loc = pygame.mouse.get_pos()
    if mouse_loc in pointlist1 or pointlist2:
        print('hi')
    # if event.type == pygame.MOUSEBUTTONDOWN:

    class Meeting:
        hovered = False

        def __init__(self, text, pos):
            self.text = text
            self.post = pos
            self.set_button()
            self.draw()

        def draw(self):
            self.set_rend()
            screen.blit(self.rend, self.button)

        def set_rend(self):
            self.rend = menu_font.render(self.text, True, self.show_text())

        def show_text(self):
            if self.hovered:
                string = 'bob'
                return string
            else:
                return (0, 0, 0)

        def set_button(self):
            self.set_rend()
            self.button = self.rend.get_button()
            self.rect.topleft = self.pos


# --------------------- CLASSES------------------------
#
#
# class TimelineModel:
#     '''
#     Encode the timeline display state
#     '''
#     def __init__(self):
#         self.timelines = []
#         for x in range():
#             timeline = Line()
#             self.timeline.append(timeline)
#         self.meeting = Meeting()
#


# class Line:
#     '''
#     Encodes the state of the line in the display
#     '''
#     def __init__(self, color, height, width, x, y):
#         self.color = color
#         self.height = height
#         self.width = width
#         self.x = x
#         self.y = y
#
#
# class Meeting:
#     '''
#     Encodes the state the meeting point circles in the game
#     '''
#     def __init__(self, color, height, width, x, y):
#         self.color = color
#         self.height = height
#         self.width = width
#         self.x = x
#         self.y = y
#
#
# class PyGameWindowView:
#     '''
#     A view of the timeline display rendered in a Pygame window
#     '''
#     def __init__(self, model, screen):
#         self.model = model
#         self.screen = screen
#
#     def draw(self):
#         self.screen.fill(pygame.Color(255, 255, 255))
#         for meeting in self.model.lines:
#
#
#     mid = int(height/2)
#
#
#     red = (200, 0, 0)
#     green = (0, 200, 0)
#     blue = (0, 0, 200)
#     white = (255, 255, 255)
#     black = (0, 0, 0)
#
#
# class PyGameMouseController:
#     '''
#     Encodes the mouse controller for it to show meeting point
#     when mouse scrolls over it
#     '''
#
# if __name__ == '__main__':
#     pygame.init()
#     size = (1200, 800)
#     screen = pygame.display.set_mode(size)
#     model = TimelineModel()
#     view = PyGameWindowView(model, screen)
#     controller = PyGameMouseController(model)
#
#     running = True
#
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEMOTION:
#                 controller.handle_mouse_event(event)
#         view.draw()
#
#     pygame.quit()


make_figure()
