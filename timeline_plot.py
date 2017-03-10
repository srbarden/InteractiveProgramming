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

import plotly.graph_objs as go

cf.go_offline()
py.init_notebook_mode()

with open('michelle_locations.json', 'r') as json_data:
    mdata = json.load(json_data)

with open('hillary_locations.json', 'r') as json_data:
    hdata = json.load(json_data)

# print(michelle_data)

shortdate = []
distance = []
description = []
location = []
title = []
for phrase in mdata:
    for article in phrase:
        shortdate.append(article['shortdate'])
        distance.append(article['distance'])
        location.append(article['location'])
        description.append(article['description'])
        title.append(article['title'])

# shortdate = [i for i, data in enumerate(shortdate)]
use_date = [d.date() for d in pd.to_datetime(shortdate)]

m_df = pd.DataFrame(
    {'Time': use_date,
     'Location': location,
     'Miles from D.C.': distance,
     'Description': description,
     'Title': title})

# print(m_df)

mm = m_df.sort_values(['Time'], ascending=True)

print(mm['Time'])

# mm.iplot(kind='scatter', title='trying')

# mm.offline.plot(kind='scatter', filename='trying')
py.plot({'data': [{'x': mm['Time'], 'y': mm['Miles from D.C.'], 'text': mm['Title']}]}, filename='lines.html')
# for phrase in mdata:
#         sorted_x = OrderedDict(sorted(phrase.items(), key=itemgetter(0)))
#         print(sorted_x)
# for phrase in mdata:
#     for article in phrase:
#         k = sorted(article.items(), key=lambda x: article['shortdate'])
#     # m_df = pd.DataFrame(phrase)
#     print(k)

# for phrase in hdata:
#     h_df = pd.DataFrame(phrase)
#     print(h_df)
