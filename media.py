class Movie(object):
    def __init__(self, title, poster, trailer, imdbID=None):
        self.trailer_youtube_url = trailer
        self.title = title
        self.poster_image_url = poster
        self.imdbID = imdbID
    def imdbUpdate(self, connection):
        if self.imdbID != None:
           self.imdbMovie = connection.get_movie(self.imdbID)
           self.title = self.imdbMovie['title']
           self.poster = self.imdbMovie['cover url']
