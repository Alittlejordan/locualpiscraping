import urllib2
import json


locu_api = '6ef01da40e3c088616da49222b245c7b69c08496'

url = 'https://api.locu.com/v1_0/venue/search/?api_key=6ef01da40e3c088616da49222b245c7b69c08496'
json_obj = urllib2.urlopen(url)

locality="name=restaurants&locality=Chicago&"


def locu_search(query):
    api_key = locu_api
    url= 'https://api.locu.com/v1_0/venue/search?api_key='+ api_key
    locality= query.replace(' ', '%20')
    final_url = url + "&locality=" + locality + "&category=restaurant"
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    
    for item in data['object']:
        print item ['name'], item['phone']