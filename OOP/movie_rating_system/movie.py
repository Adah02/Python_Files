from movie_rating_system import rating

class Movie:
    def __init__(self, title):
        self.title = title
        self.movies = []

    @staticmethod
    def movie_date_and_time():
        from datetime import datetime
        date_time = datetime.now()
        hour = date_time.hour
        if hour > 12:
            hour = hour % 12
        date_and_time = date_time.strftime(f"%d %m %Y  {hour}:%M %p")
        return date_and_time

    def add_movie(self, title):
        #For adding a movie to the list
        rate = rating.Rating()
        self.movies.append({"name":title, "date": self.movie_date_and_time()})
        rate.add_rating_list([])

    def movie_list(self):
        return self.movies
