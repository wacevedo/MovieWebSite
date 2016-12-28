import webbrowser

class Video(object):
    """This class is the parent:
    like the general for all content Video

    Attributes:
        title               (str): This attributes contain the name of the video content
        storyline           (str): This attributes contain a resume of the video content
        poster_image_url    (str): This attributes contain an image of the video content
        trailer_youtube_url (str): This attributes contain an URL of the trailer of the video content
    """
    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
    """This class provided a way to store movie

    Attributes:
        movie_runtime (int): This attributes contain the length of the movie on hours

    """

    def __init__(self, movie_title, movie_runtime, movie_storyline,
                 movie_poster_image_url, movie_trailer_youtube_url):
        super(Movie, self).__init__(movie_title, movie_storyline,
              movie_poster_image_url, movie_trailer_youtube_url)
        self.movie_runtime = movie_runtime


class Tv_Show(Video):
    """This class provided a way to store Tv Shows

    Attributes:
        number_of_seasons  (str): This attributes contain the number of seasons
        number_of_episodes (str): This attributes contain the number of episodes

    """

    def __init__(self, tv_title, number_of_seasons, number_of_episodes,
                 tv_storyline, tv_poster_image_url, tv_trailer_youtube_url):
        super(Tv_Show, self).__init__(tv_title, tv_storyline, tv_poster_image_url,
              tv_trailer_youtube_url)
        self.number_of_seasons = number_of_seasons
        self.number_of_episodes = number_of_episodes