import json
import numpy as np
import pandas as pd
import collections
from collections import OrderedDict
from collections import defaultdict
from operator import itemgetter
from datetime import date
import plotly

import plotly.offline as offline
import plotly.graph_objs as go

with open('michelle_locations.json', 'r') as json_data:
    mdata = json.load(json_data)

with open('hillary_locations.json', 'r') as json_data:
    hdata = json.load(json_data)

# print(michelle_data)

shortdate = []
distance = []
description = []
for phrase in mdata:
    for article in phrase:
        shortdate.append(article['shortdate'])
        distance.append(article['distance'])
        description.append(article['description'])

shortdate = [i for i, data in enumerate(shortdate)]

print(shortdate)
print(distance)

offline.init_notebook_mode()
# offline.plot({'data': [{'y': [4, 2, 3, 4]}],
#                'layout': {'title': 'Test Plot',
#                           'font': dict(size=16)}},
#              image='png')

# mtrace = go.Scatter(x=shortdate, y=distance)
offline.plot({'data': [{'x': shortdate, 'y': distance}]}, image='png')
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
