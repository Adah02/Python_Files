from movie_rating_system.movie_ratings.rating import Rating

class Movie:
    def __init__(self):
        self.rate = Rating()
        self.movies = []

    @staticmethod
    def movie_date():
        from datetime import date
        date = date.today()
        year = date.year
        month = date.month
        day = date.day
        return year, month, day

    def add_movie(self, title):
        #For adding a movie to the list
        self.movies.append({"name":title, "date": self.movie_date()})
        self.rate.add_rating_list([])

    def movie_list(self):
        return self.movies
