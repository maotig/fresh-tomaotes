#!/usr/bin/env python
#
# Project 1 - Movie Trailer Webpages - class
# Author: Jeremy Puhhlman
# Class definition for Movie, to be passed to fresh_tomatoes.py
#
# Copyright (c) 2015 Jeremy Puhlman.  All rights reserved.
#
# Released under the MIT license (see LICENSE.MIT for the terms)
#


class Movie(object):
    """Class for containing infromation for a movie catalog.

    Attributes:
        title(str): Name of the movie
        poster(str): Url to movie box art image
        trailer(str): Url to Youtub video tailer for movie
        imdb_id(str): IMDB id number for movie.
        imdb_sync(bool): Set if imdb_update has successfully populated
                        the its data
    """
    def __init__(self, title, poster, trailer, imdb_id=None):
        """ Init used for standard and extended movie content
        prams:
            title(str): Name of the movie
            poster(str): Url to movie box art image
            trailer(str): Url to Youtub video tailer for movie
            imdb_id(str): IMDB id number for movie. Defaults to None.
        """
        self.trailer_youtube_url = trailer
        self.title = title
        self.poster_image_url = poster
        self.imdb_id = imdb_id
        self.imdb_sync = False

    def imdb_update(self, connection):
        """ Function to populate imdb data if a conntection is available
        params:
            connection(imdb.movie): IMDB movie object
        """
        if self.imdb_id != None:
           self.imdb_movie = connection.get_movie(self.imdb_id)
           self.title = self.imdb_movie['title']
           self.poster = self.imdb_movie['full-size cover url']
           self.year = self.imdb_movie['year']
           self.cast = self.parse_person_list(self.imdb_movie['cast'])
           self.imdb_sync = True

    def parse_person_list (self, person_list):
        """ Create a list of the top 10 attributed actors
        params:
            person_list(list): full cast list returned from imdb movie object
        returns:
            (list): Top 10 attributed actors from person_list
        """
        max_persons = 10
        num_persons = len(person_list)
        name_list = []
        if num_persons < 10:
           max_persons = num_persons - 1
        for person in person_list[0:max_persons]:
            name_list.append(person["name"])
        return ",".join(name_list)

    def imdb_catalog(self):
        """ Return if the imdb content population has been successful
        returns:
            (boot): True if imdb_update has successfully run.
                    Fales if it has not.
        """
        return self.imdb_sync
