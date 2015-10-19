#!/usr/bin/env python
#
# Project 1 - Movie Trailer Webpage
# Author: Jeremy Puhhlman
# This project will work with or with out the python imdb
# module installed. With the module installed additional
# information is added to the webpage.
#
# Usages of imdbpy, are developed from the examples and api documentation
# provided at http://imdbpy.sourceforge.net/
#
# Copyright (c) 2015 Jeremy Puhlman.  All rights reserved.
#
# Released under the MIT license (see LICENSE.MIT for the terms)
#


import media
import fresh_tomatoes

# Check if imdb is installed.
# If not fall back on simpler pages called out by project.
try:
   import imdb
   imdbSupported = True
except ImportError:
   imdbSupported = False

# Create movile catalog
# For each movie add:
# Name
# Link to box art
# Link to YouTube video for trailer
# IMDB id value, for use if imdb module is installed
def get_static_catalog():
    """ Setup static catalog of movie for passing to fresh_tomoatoes.py
    returns:
        (list): List of media.Movie objects.
    """
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

# If imdb module installed, pass imdb connection to movie object to update
# content with imdb content
def get_imdb_catalog():
    """ Connect to imdb database to retrieve additional move information
    returns:
        (list): List of media.Movie objects after updating imdb content
    """
    imdb_connection = imdb.IMDb()
    catalog = get_static_catalog()
    for movie in catalog:
        movie.imdb_update(imdb_connection)
    return catalog

def main():
    """ Main function """
    if imdbSupported:
       fresh_tomatoes.open_movies_page(get_imdb_catalog())
    else:
       fresh_tomatoes.open_movies_page(get_static_catalog())

if __name__ ==  "__main__":
    main()

