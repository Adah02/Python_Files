from movie_rating_system import rating

class Movie:
    def __init__(self, title):
        self.title = title
        self.rate = rating.Rating()
        self.movies = []

    @staticmethod
    def movie_date_and_time():
        from datetime import datetime
        time = datetime.now()
        hour = time.hour
        if hour > 12:
            hour = hour % 12
        date_and_time = time.strftime(f"%d %m %Y  {hour}:%M %p")
        return date_and_time

    def add_movie(self, title):
        #For adding a movie to the list
        self.movies.append({"name":title, "date": self.movie_date_and_time()})
        self.rate.add_rating_list([])

    def movie_list(self):
        return self.movies
