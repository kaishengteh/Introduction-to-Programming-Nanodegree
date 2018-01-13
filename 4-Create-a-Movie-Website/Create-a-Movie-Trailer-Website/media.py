import webbrowser
   
class Movie():

#This class stores related information about movie and initialize instance of class Movie

  def __init__(self, movie_title, movie_review, poster_image, trailer_youtube, release_year):
    self.title = movie_title
    self.review = movie_review
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube
    self.year = release_year

  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
