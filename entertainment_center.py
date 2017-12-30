import os
import media
import fresh_tomatoes

def load_movies():
    #Load movies from text file
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'movies.txt')
    f = open(my_file, 'r')
    movie_list = f.read().splitlines()
    f.close()
    
    movies=[]
    #Instantiate each movie and add reference to movies[] list
    for movie_item in movie_list:
        movie_attributes = movie_item.split(',')
        movies.append(media.Movie(movie_attributes[0],
                                    movie_attributes[1],
                                    movie_attributes[2]))
        
    #Generate static web page of movies
    fresh_tomatoes.create_movies_page(movies)