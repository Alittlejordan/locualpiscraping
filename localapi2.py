import urllib2
import json

locu_api = '6ef01da40e3c088616da49222b245c7b69c08496"'

url = 'https://api.locu.com/v1_0/venue/search/?name=burger&locality=florida&api_key=6ef01da40e3c088616da49222b245c7b69c08496'
json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

for item in data ['objects']:
    print item['country']
    print item['website_url']