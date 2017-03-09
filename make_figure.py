from plotly.graph_objs import Scatter, Figure, Layout
from compute_distances import compute_distances()

distances = compute_distances()

def make_figure():
    width = 1200
    height = 800
    mid = int(height/2)

# --------- DRAWING LINES AND POINTS--------------------------------
    ylist = []
    xlist = []
    for key in distances:
        dist = distances[key]  # scale down distances

        point1 = mid - 0.5*dist  # calculates points for person 1
        point2 = mid + 0.5*dist  # calculates points for person 2

        year = int(key[0:4])
        month = int(key[5:7])
        day = int(key[8:10])
        t = datetime.date(year, month, day)

        x = (t - datetime.date(1990, 1, 1)).total_seconds()

        y1 = point1
        y2 = point2

        ylist.append(y1)
        xlist.append(x)

    plot([Scatter(x=xlist, y=ylist)])

    if dist == 0:
        meetings.append((key, mid))


make_figure()
