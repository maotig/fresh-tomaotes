#!/usr/bin/env python

import media
import fresh_tomatoes
try:
   import imdb
   imdbSupported = True
except ImportError:
   imdbSupported = False
   
def getStaticCatalog():
    movies = []
    movies.append(media.Movie("Star Wars",
                         "http://ia.media-imdb.com/images/M/MV5BMTU4NTczODkwM15BMl5BanBnXkFtZTcwMzEyMTIyMw@@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=ba2TH-K7oiA",
                          "0076759"))
    movies.append(media.Movie("Fifth Element",
                         "http://ia.media-imdb.com/images/M/MV5BMTkzOTkwNTI4N15BMl5BanBnXkFtZTYwMDIzNzI5._V1_SY317_CR6,0,214,317_AL_.jpg",
                         "https://www.youtube.com/watch?v=aB-AUTGqUCU",
                         "0119116"))
    movies.append(media.Movie("Star Trek II: The Wrath of Khan",
                         "http://ia.media-imdb.com/images/M/MV5BMTcwNjc5NjA4N15BMl5BanBnXkFtZTcwNDk5MzI4OA@@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=vOIYaRb6XpQ",
                         "0084726"))
    movies.append(media.Movie("Big Lebowski",
                         "http://ia.media-imdb.com/images/M/MV5BMTQ0NjUzMDMyOF5BMl5BanBnXkFtZTgwODA1OTU0MDE@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=cd-go0oBF4Y",
                         "0118715"))
    movies.append(media.Movie("The Matrix",
                         "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=Q8g9zL-JL8E",
                         "0133093"))
    movies.append(media.Movie("Pink Floyd The Wall",
                         "http://ia.media-imdb.com/images/M/MV5BMTcxMDAzNDk2M15BMl5BanBnXkFtZTYwNDE4MDg4._V1_SY317_CR4,0,214,317_AL_.jpg",
                         "https://www.youtube.com/watch?v=PEQEgpyrQ3Q",
                         "0084503"))
    return movies
def getImdbCatalog():
    imdb_connection = imdb.IMDb()
    catalog = getStaticCatalog()
    for movie in catalog:
        movie.imdbUpdate(imdb_connection)
    return catalog
def main():
    if imdbSupported:
       fresh_tomatoes.open_movies_page_extras(getImdbCatalog())
    else:
       fresh_tomatoes.open_movies_page(getStaticCatalog())

if __name__ ==  "__main__":
    main()

