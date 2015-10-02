class Movie(object):
    def __init__(self, title, poster, trailer):
        self.trailer_youtube_url = trailer
        self.title = title
        self.poster_image_url = poster
