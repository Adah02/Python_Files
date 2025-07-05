from movie_rating_system.movie_ratings import movie

from unittest import TestCase

class TestMovieRatingApp(TestCase):
    def test_that_movie_list_isEmpty(self):
        self.assertFalse(False, movie.movie_list())

        movie_rating_app.add_movie("Semicolon")
        self.assertTrue(True, movie_rating_app.movie_list())

    def test_that_movie_list_isNotEmpty(self):
        movie_rating_app.add_movie("Semicolon")
        self.assertTrue(True, movie_rating_app.movie_list())

    def test_that_rating_list_isEmpty(self):
        self.assertTrue(True, movie_rating_app.rating_list())

        movie_rating_app.rate_movie("Semicolon", 4)
        self.assertFalse(False, movie_rating_app.rating_list())

    def test_that_rating_list_isNotEmpty(self):
        movie_rating_app.rate_movie("Semicolon", 4)
        self.assertTrue(True, movie_rating_app.rating_list())

    def test_average_rating_for_a_movie(self):
        movie_rating_app.add_movie("Semicolon")
        movie_rating_app.add_movie("Semi")
        movie_rating_app.rate_movie("Semicolon", 4)
        movie_rating_app.rate_movie("Semicolon", 5)
        movie_rating_app.rate_movie("Semicolon", 3)

        self.assertEqual(4, movie_rating_app.average_rating_for_each_movie("Semicolon"))

    def test_total_average_ratings(self):
        movie_rating_app.add_movie("Semicolon")
        movie_rating_app.add_movie("Semi")
        movie_rating_app.rate_movie("Semicolon", 4)
        movie_rating_app.rate_movie("Semicolon", 5)
        movie_rating_app.rate_movie("Semi", 3)
        movie_rating_app.rate_movie("Semi", 2)

        self.assertEqual(3.5, movie_rating_app.average_ratings_for_all_movies())

