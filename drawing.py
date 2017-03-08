#  Drawing lines given the distance apart
#  draws symmetrically aorund center axis

import pygame


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

# ---------- MOUSE EVENT ---------------------------------------
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
