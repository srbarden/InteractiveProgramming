#  Drawing lines given the distance apart
#  draws symmetrically aorund center axis

import pygame


def draw():
    pygame.init()
    width = 1200
    height = 800
    screen = pygame.display.set_mode((width, height))

    red = (255, 0, 0)
    blue = (0, 0, 255)
    white = (0, 0, 0)

    # maps hypothetical times and distance between two people
    distances = {1: 200, 2: 150, 3: 50, 4: 0, 5: 100, 6: 200}

    # this keeps the window open
    done = False
    clock = pygame.time.Clock()
    while not done:
        clock.tick(10)  # 10 times per second through hte loop
        for event in pygame.event.get():  # for an event
            if event.type == pygame.QUIT:  # if you click close
                done = True   # done to exit this loop

        screen.fill(white)  # supposed to make screen white
        pointlist1 = []
        pointlist2 = []
        for key in distances:
            dist = distances[key]
            mid = height/2
            point1 = mid - 0.5*dist
            point2 = mid + 0.5*dist
            pointlist1.append((key*100, point1))
            pointlist2.append((key*100, point2))
        pygame.draw.lines(screen, blue, False, pointlist1, 2)
        pygame.draw.lines(screen, red, False, pointlist2, 2)
        pygame.display.update()


draw()
