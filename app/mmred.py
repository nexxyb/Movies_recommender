import requests
import json
import config

def get_movies_from_tastedive(name):
    #go to https://tastedive.com/api to get your api key
    api_key = config.api_key
    parameters= {}
    parameters['q'] = name
    parameters['type'] = 'movie'
    parameters['limit'] = 5
    parameters['k'] = api_key
    response = requests.get('https://tastedive.com/api/similar', params= parameters)
    #page = json.dumps(response.text)
    return response.json()

print(get_movies_from_tastedive("black panther"))