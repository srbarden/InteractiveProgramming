import indicoio
import json
# from indico_knock import Indico_KEY
indicoio.config.api_key = '9849e59cdcf05c8f6eaecd7bd78a4add'

# j = indicoio.places("U.S. first lady Michelle Obama meets with the children ", threshold=0.01)
# print(j)


with open('michelle_data2.json', 'r') as json_data:
    michelle_news = json.load(json_data)

with open('hillary_data2.json', 'r') as json_data:
    hillary_news = json.load(json_data)


print(len(michelle_news))
print(len(michelle_news[2]))
for i in michelle_news:
    for j in i:
        print(j)

print(len(hillary_news))
print(len(hillary_news[0]))
for i in hillary_news:
    for j in i:
        print(j)
