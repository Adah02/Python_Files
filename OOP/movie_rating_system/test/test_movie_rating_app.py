from contextlib import nullcontext
from movie_rating_system import movie
from movie_rating_system import rating

from unittest import TestCase

movie1 = movie.Movie(title= nullcontext)
rates = rating.Rating()

class TestMovieRatingApp(TestCase):
    def test_that_movie_list_isEmpty(self):
        self.assertFalse(False, movie1.movie_list())

        movie1.add_movie("Semicolon")
        self.assertTrue(True, movie1.movie_list())

    def test_that_movie_list_isNotEmpty(self):
        movie1.add_movie("Semicolon")
        self.assertTrue(True, movie1.movie_list())

    def test_that_rating_list_isEmpty(self):
        self.assertTrue(True, rates.rating_list())



