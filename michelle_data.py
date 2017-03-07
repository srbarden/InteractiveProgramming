import json
import indicoio
from indico_knock import Indico_KEY

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
