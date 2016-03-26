import webbrowser

class Movie():
    """ 
    Create a Movie class to help display and call some of my favorite movies.
    """

    def __init__(self, movie_title, movie_info, poster_image,trailer_youtube):
        """
        Call the information for an instance of the Movie class.
        """
        self.title = movie_title
        self.imdb_link = movie_info
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
