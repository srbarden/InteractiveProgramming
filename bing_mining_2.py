'''
    Sarah Barden and Alisha Pegan
    March 7th, 2017
    SoftDesign
    Data Visualization
    Code to extract news articles from Bing regarding where Hillary Clinton
    and Michelle Obama have traveled
'''
import json
import requests
from bing_knock import BING_KEY
import indicoio
from indico_knock import Indico_KEY
indicoio.config.api_key = Indico_KEY
# dir({})


def bing_search(query, name):
    # base API url
    url = 'https://api.cognitive.microsoft.com/bing/v5.0/news/search'
    # url += '?$format=json&$top=1&Query=%27{}%27'.format(quote_plus(query))
    # count max at 100
    # url += '?q={}&count=10'.format(quote_plus(query))
    url += '?q={}&count=100'.format((query))
    headers = {'Ocp-Apim-Subscription-Key': BING_KEY}
    r = requests.get(url, headers=headers)
    resp = json.loads(r.text)
    # print(len(resp['value']))
    # print(resp)
    news = []
    # after studying the json, learned what the data structure is
    # set up is dictionary > list > dictionary
    # need to call the data in the right format
    for article in resp["value"]:
        if name in article['name']:
            place = indicoio.places(article['name'])
            # if there is content in the places, store it in a dic
            if len(place) > 0:
                temp_dic = {}
                temp_dic['title'] = article['name']
                temp_dic['location'] = place[0]['text']
                temp_dic['description'] = article['description']
                temp_dic['date_pub'] = article['datePublished']
                temp_dic['url'] = article['url']
                news.append(temp_dic)
    # print(news)
    return news


# michelle obama search phrases
# needs to be exact string
michelle_phrases = ['"Michelle+Obama+travels+to"',
                    '"Michelle+Obama+travelled+to"',
                    '"Michelle+Obama+arrives+in"',
                    '"Michelle+Obama+meets+with"']

# hillary clinton search phrases
hillary_phrases = ['"Hillary+Clinton+travels+to"',
                   '"Hillary+Clinton+travelled+to"',
                   '"Hillary+Clinton+arrives+in"',
                   '"Hillary+Clinton+meets+with"',
                   '"Hillary+Clinton+arrives+to"'
                   '"Hillary+Clinton+arrvies+at"']

for phrase in michelle_phrases:
    michelle_results = bing_search(phrase, 'Michelle Obama')
    # print(michelle_results)

for phrase in hillary_phrases:
    hillary_results = bing_search(phrase, 'Hillary Clinton')
    # print(hillary_results)
    print(len(hillary_results))

with open('michelle_data.json', 'w') as outfile:
    json.dump(michelle_results, outfile)

with open('hillary_data.json', 'w') as outfile:
    json.dump(hillary_results, outfile)
