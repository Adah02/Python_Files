from movie_rating_system.rating import Rating
from movie_rating_system.movie_rating import Movie
from unittest import TestCase

class TestMovieRatingApp(TestCase):

    def test_that_movie_list_isEmpty(self):
        movi = Movie()
        self.assertEqual(movi.movie_list(), [])

    def test_that_rating_list_isEmpty(self):
        rate = Rating()
        self.assertEqual(rate.rating_list(), [])

    def test_that_movie_is_added(self):
        movi = Movie()
        movi.add_movie("Semicolon")
        self.assertEqual([{'date': '12 07 2025  3:20 PM', 'name': 'Semicolon'}], movi.movie_list())

    def test_that_rating_list_is_added(self):
        rate = Rating()
        movi = Movie()
        movi.add_movie("Semicolon")
        rate.add_rating_list([])
        self.assertEqual([[]], rate.rating_list())

    def test_that_movie_can_be_removed(self):
        movi = Movie()
        movi.add_movie("Semicolon")
        rate = Rating()
        rate.add_rating_list([])

        self.assertEqual([[]], rate.rating_list())
