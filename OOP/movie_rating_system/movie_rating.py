class Movie:
    def __init__(self):
        self.movies = []
        self.ratings = []

    @staticmethod
    def movie_date_and_time():
        from datetime import datetime
        date_time = datetime.now()
        hour = date_time.hour
        if hour > 12:
            hour = hour % 12
        elif hour == 0:
            hour = 12
        date_and_time = date_time.strftime(f"%d %m %Y  {hour}:%M %p")
        return date_and_time

    def add_movie(self, title):
        #For adding a movie to list
        self.movies.append({"name":title, "date": self.movie_date_and_time()})
        self.ratings.append([])

    def rate_movie(self,title, rating):
        # For rating a movie
        for count in range(len(self.movies)):
            if self.movies[count]["name"].lower() == title.lower():
                self.ratings[count].append(rating)

    def remove_movie(self, title):
        for index, movie in enumerate(self.movies):
            if movie["name"].lower() == title.lower():
                self.movies.remove(self.movies[index])
                self.ratings.remove(self.ratings[index])

    def movie_list(self):
        return self.movies

    def average_rating_for_movie(self):
        #For calculating average movie ratings
        for count in range(len(self.movies)):
            try:
                print(f"Movie name: {self.movies[count]["name"]}  -> Average Rating: {(sum(self.ratings[count])) / len(self.ratings[count])}")
            except ZeroDivisionError:
                print(f"Movie name: {self.movies[count]["name"]}  -> Average Rating: 0")

    def movie_list_and_ratings(self):
        #To view movie ratings and the respective ratings
        for index, movie in enumerate(self.movies):
            try:
                print(f"{movie['name']} : {self.ratings[index]}")
            except IndexError:
                print(f"{movie['name']} ")

    def rating_list(self):
        return self.ratings