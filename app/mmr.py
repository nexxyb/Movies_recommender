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

#print(get_movies_from_tastedive("black panther"))

def extract_movie_titles(result_function):
    titles=[]
    title_list= result_function['Similar']['Results']
    for result in title_list:
        titles.append(result['Name'])
    return titles   
    
#print(extract_movie_titles(get_movies_from_tastedive("black panther")))

def get_related_titles(titles):
    related_titles = []
    for title in titles:
        each_title= extract_movie_titles(get_movies_from_tastedive(title))
        for new_title in each_title:
            if new_title not in related_titles:
                related_titles.append(new_title)
    return related_titles  
    
        
#print(get_related_titles(["the witcher"]))

def get_movie_data(movie_title):
    
    parameters= {}
    parameters['t'] = movie_title
    parameters['type'] = 'movie'
    parameters['apikey'] = config.api_key2
    response = requests.get('http://www.omdbapi.com/', params= parameters)
    #page = json.dumps(response.text)
    #print(response)
    res =  response.json()
    #print(res)
    if res['Response'] == 'True':
        return res
    else:
        return 'N/A'

#print(get_movie_data("matrix"))

def get_movie_rating(movie):
    mov_details= get_movie_data(movie)
    #print(mov_details)
    if type(mov_details) == dict:
        #print(mov_details)
        ratings= mov_details['Ratings']
        #print(ratings)
        if len(ratings) >= 1:
            rating = ratings[0]
            if rating['Source'] == 'Internet Movie Database':
                act_rating= rating['Value']
                if act_rating == '0%' or act_rating == None :
                    return 0
                else:
                    actual_rating= float(act_rating[:3])
                    return actual_rating
            else:
                return 'N/A'
        else:
            return 'N/A'
    else:
        return 'N/A'
#print(get_movie_rating("the protege"))

    
def get_movie(movie_list):
    recommendations= []
    recom1= []
    recom2 = []
    for movie in movie_list:
        related_titles = get_related_titles(movie_list) 
        for movie in related_titles:
            movie_rating = get_movie_rating(movie)
            recommendations.append((movie_rating,movie))
        for pair in recommendations:
            if type(pair[0]) == float:
                recom1.append(pair)
            else:
                recom2.append(pair)
        recommended= sorted(recom1, reverse=True) + recom2
        return recommended
print(get_movie('unfaithful'))
    
