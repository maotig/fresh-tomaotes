#!/usr/bin/env python

import media
import fresh_tomatoes
#import imdb

def main():
    movies = []
    starwars = media.Movie("Star Wars",
                         "http://ia.media-imdb.com/images/M/MV5BMTU4NTczODkwM15BMl5BanBnXkFtZTcwMzEyMTIyMw@@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=ba2TH-K7oiA")
    fifthelement = media.Movie("Fifth Element",
                         "http://ia.media-imdb.com/images/M/MV5BMTkzOTkwNTI4N15BMl5BanBnXkFtZTYwMDIzNzI5._V1_SY317_CR6,0,214,317_AL_.jpg",
                         "https://www.youtube.com/watch?v=aB-AUTGqUCU")
    startrektwo = media.Movie("Star Trek II: The Wrath of Khan",
                         "http://ia.media-imdb.com/images/M/MV5BMTcwNjc5NjA4N15BMl5BanBnXkFtZTcwNDk5MzI4OA@@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=vOIYaRb6XpQ")
    biglebowski = media.Movie("Big Lebowski",
                         "http://ia.media-imdb.com/images/M/MV5BMTQ0NjUzMDMyOF5BMl5BanBnXkFtZTgwODA1OTU0MDE@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=cd-go0oBF4Y")
    matrix = media.Movie("The Matrix",
                         "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=Q8g9zL-JL8E")
    thewall = media.Movie("The Wall",
                         "http://ia.media-imdb.com/images/M/MV5BMTcxMDAzNDk2M15BMl5BanBnXkFtZTYwNDE4MDg4._V1_SY317_CR4,0,214,317_AL_.jpg",
                         "https://www.youtube.com/watch?v=PEQEgpyrQ3Q")
    
    movies += [starwars,fifthelement,startrektwo, biglebowski, matrix, thewall]
    fresh_tomatoes.open_movies_page(movies)

if __name__ ==  "__main__":
    main()

