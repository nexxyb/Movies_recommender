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
    parameters['info'] =1
    parameters['k'] = api_key
    response = requests.get('https://tastedive.com/api/similar', params= parameters)
    return response.json()


def extract_movie_titles(result_function):
    titles=[]    
    title_list= result_function['Similar']['Results']
    for result in title_list:
        titles.append((result['Name'], result['yUrl']))
    return titles 


def get_related_titles(title):
    related_titles = []
    each_title= extract_movie_titles(get_movies_from_tastedive(title))    
    for new_title in each_title:        
        if new_title[0] not in related_titles:
            related_titles.append(new_title)
    return related_titles  


def get_movie_data(movie_title):
    #go to https://omdbapi.com to get your api key
    parameters= {}
    parameters['t'] = movie_title
    parameters['type'] = 'movie'
    parameters['apikey'] = config.api_key2
    response = requests.get('http://www.omdbapi.com/', params= parameters)
    res =  response.json()
    if res['Response'] == 'True':
        return res
    else:
        return 'N/A'


def get_movie_rating(movie):
    mov_details= get_movie_data(movie)    
    if type(mov_details) == dict:        
        ratings= mov_details['Ratings']        
        if len(ratings) >= 1:
            rating = ratings[0]
            if rating['Source'] == 'Internet Movie Database':
                act_rating= rating['Value']
                if act_rating == '0%' or act_rating == None :
                    actual_rating= 0
                else:
                    actual_rating= float(act_rating[:3])                    
            else:
                actual_rating= 0       
        else:
            actual_rating= 0
        actors= mov_details['Actors']
        plot= mov_details['Plot']
        movie_details=[actual_rating,actors,plot]        
        return movie_details 
        
def get_movie(movie_list):
    movie_list=[movie_list]    
    main_movie_list= []
    main_movie_details = []
    movies_lists= []
    for m in movie_list:
        movies_lists.append(m.lower())
    for movie in movies_lists:
        related_titles = get_related_titles(movie_list) #list of tuples
        for movie in related_titles:
            movie_rating = get_movie_rating(movie[0]) # list
            main_movie_list.append(movie[0])
            movie_rating.append(movie[1])
            main_movie_details.append(movie_rating)       
    movie_dict= dict(zip(main_movie_list, main_movie_details))
    recom= {k:v for k,v in sorted(movie_dict.items(), key=lambda item: item[1][0], reverse=True)}
    return recom
