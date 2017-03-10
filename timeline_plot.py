import json
import numpy as np
import pandas as pd
import collections
from collections import OrderedDict
from collections import defaultdict
from operator import itemgetter
import datetime
from datetime import date
import plotly
import plotly.offline as py
import cufflinks as cf

cf.go_offline()
py.init_notebook_mode()

with open('michelle_locations.json', 'r') as json_data:
    mdata = json.load(json_data)

with open('hillary_locations.json', 'r') as json_data:
    hdata = json.load(json_data)

# -----------Putting Data Into A DataFrame--------------
'''
function dataframe takes all the data out from the current
data structure, and sets it up properly to plot on plotly
'''


def dataframe(data):
    # great empty lists to store data
    shortdate = []
    distance = []
    description = []
    location = []
    title = []
    # loop through the lists
    for phrase in data:
        # loop through the lists
        for article in phrase:
            # extract the data from the dictionaries
            shortdate.append(article['shortdate'])
            distance.append(article['distance'])
            location.append(article['location'])
            description.append(article['description'])
            title.append(article['title'])

    # convert shortdate from string to datetime
    use_date = [d.date() for d in pd.to_datetime(shortdate)]
    # alternative: shortdate = [i for i, data in enumerate(shortdate)]
    # set it up as a dataframe
    df = pd.DataFrame(
        {'Time': use_date,
         'Location': location,
         'Miles from D.C.': distance,
         'Description': description,
         'Title': title})

    # sort the dataframe by the date, most recent to least
    sorted_df = df.sort_values(['Time'], ascending=True)
    return sorted_df


# -------------Plotting Data------------------------

m_df = dataframe(mdata)
h_df = dataframe(hdata)
fig = {
    'data': [
        {'x': m_df['Time'], 'y': -m_df['Miles from D.C.'],
         'text': m_df['Title'],
         'name': 'Michelle Obama'},
        {'x': h_df['Time'], 'y': h_df['Miles from D.C.'],
         'text': h_df['Title'],
         'name': 'Hillary Clinton'}
    ],
    'layout': {
        'xaxis': {'title': 'Year'},
        'yaxis': {'title': "Distance from D.C."}
    }
}

py.plot(fig, filename='timelines.html')

# py.plot({'data': [{'x': mm['Time'], 'y': mm['Miles from D.C.'], 'text': mm['Title']}]}, filename='lines.html')
