#  Drawing lines given the distance apart
#  draws symmetrically aorund center axis

import pygame


def draw():
    pygame.init()
    width = 1200
    height = 800
    mid = height/2
    screen = pygame.display.set_mode((width, height))

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    purple = (200, 0, 200)
    white = (0, 0, 0)

    # maps hypothetical times and distance between three people
    distances12 = {1: 200, 2: 50, 3: 50, 4: 0, 5: 100, 6: 0}
    distances23 = {1: 50, 2: 0, 3: 100, 4: 0, 5: 100, 6: 100}
    distances31 = {1: 100, 2: 50, 3: 100, 4: 0, 5: 0, 6: 100}

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
        pointlist3a = []
        pointlist3b = []
        for key in distances12:
            dist12 = distances12[key]
            dist23 = distances23[key]

            point1 = mid - 0.5*dist12
            point2 = mid + 0.5*dist12

            pointlist1.append((key*150, point1))
            pointlist2.append((key*150, point2))

        pygame.draw.lines(screen, red, False, pointlist1, 2)
        pygame.draw.lines(screen, green, False, pointlist2, 2)

        pygame.display.update()

    mouse_loc = pygame.mouse.get_pos()
    if mouse_loc in pointlist1 or pointlist2:
        print('hi')
    # if event.type == pygame.MOUSEBUTTONDOWN:


draw()
