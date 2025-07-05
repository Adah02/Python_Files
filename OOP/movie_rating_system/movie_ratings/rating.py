from movie import Movie

class Rating:
    def __init__(self):
        self.ratings = []
        movie = Movie()
        self.movies = movie.movie_list()

    def add_rating_list(self, list):
            self.ratings.append(list)

    def rate_movie(self,title, rating):
        # For rating a movie
        for count in range(len(self.movies)):
            if self.movies[count]["name"].lower() == title.lower():
                self.ratings[count].append(rating)

    def average_rating_for_movie(self, title):
        average = 0
        for count in range(len(self.movies)):
            if self.movies[count]["name"].lower() == title.lower():
                average = sum(self.ratings[count]) / len(self.ratings[count])
        return average

    def average_ratings_for_all_movies(self):
        #To get average ratings for all movies
        average = 0
        for index in range(len(self.ratings)):
            average += sum(self.ratings[index]) / len(self.ratings[index])

        total_average = average / len(self.ratings)
        return float(f'{total_average:.1f}')

    def rating_list(self):
        return self.ratings