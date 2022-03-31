#This program gets 5 related movies for every movie you input
#and sorts by IMDb rating

import requests
import json
#define function that get movies similar to the given title from
#tastedive.com api
#you will need to request api key from https://tastedive.com/read/api
def get_movies_from_tastedive(name):
    api_key = '434663-movierec-4WFEAXZ0'
    parameters= {}
    parameters['q'] = name
    parameters['type'] = 'movie'
    parameters['limit'] = 5
    parameters['k'] = api_key
    response = requests.get('https://tastedive.com/api/similar', params= parameters)
    return response.json()


#Define function that extract the titles from result of the above function
def extract_movie_titles(result_function):
    titles=[]
    title_list= result_function['Similar']['Results']
    for result in title_list:
        titles.append(result['Name'])
    return titles   
    

def get_related_titles(titles):
    related_titles = []
    for title in titles:
        each_title= extract_movie_titles(get_movies_from_tastedive(title))
        for new_title in each_title:
            if new_title not in related_titles:
                related_titles.append(new_title)
    return related_titles  
    
        

def get_movie_data(movie_title):
    #api_key = 'f8e4a135'
    parameters= {}
    parameters['t'] = movie_title
    parameters['type'] = 'movie'
    parameters['apikey'] = ['f8e4a135']
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

    
def get_sorted_recommendations(movie_list):
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

print(get_sorted_recommendations(["Awake","sweet girl","unfaithful"]))
    

