import os
import media
import fresh_tomatoes

def load_movies():
    #load movies from text file
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'movies.txt')
    f = open(my_file, 'r')
    movie_list = f.read().splitlines()
    f.close()
    
    movies=[]
    for movie_item in movie_list:
        movie_attributes = movie_item.split(',')
        movies.append(media.Movie(movie_attributes[0],
                                    movie_attributes[1],
                                    movie_attributes[2]))
        
    fresh_tomatoes.open_movies_page(movies)