import requests
import json
def get_movies_from_tastedive(name):
    #go to https://tastedive.com/api to get your api key
    api_key = 'insert key here'
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
    #api_key = 'f8e4a135'
    parameters= {}
    parameters['t'] = movie_title
    parameters['type'] = 'movie'
    parameters['apikey'] = ['f8e4a135']
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

    
def get_sorted_recommendations(movie_list):
    l_movie_list= []
    for m in movie_list:
        l_movie_list.append(m.lower())
    #print(l_movie_list)
    recommendations= []
    final_recommendations= []
    for movie in l_movie_list:
        related_titles = get_related_titles(movie_list)
        
        #print(related_titles)
        for movie in related_titles:
            movie_rating = get_movie_rating(movie)
            recommendations.append((movie, movie_rating))
        for pair in recommendations:
            if pair[0].lower() not in l_movie_list:
                final_recommendations.append(pair)
        
        recommended= sorted(final_recommendations, reverse= True, key= lambda x: x[1])
        return recommended

print(get_sorted_recommendations(["Basic Instinct","Unfaithful","Killing me softly"]))
    
