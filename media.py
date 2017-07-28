# Create Movie Class #


class Movie():
    """
    Define your parameters for the movie class.
    You can call the title, story, poster, and trailer vars
    whatever you'd like or is easy for your to remember.
    **Note** Don't change the name of what the variables will store to(left)
    Only (right) and within the init f(x).
    """
    def __init__(self, mov_title, mov_story, mov_poster, mov_trailer):
        self.title = mov_title
        self.storyline = mov_story
        self.poster_image_url = mov_poster
        self.trailer_youtube_url = mov_trailer
