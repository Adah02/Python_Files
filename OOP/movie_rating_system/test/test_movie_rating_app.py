from movie_rating_system.rating import Rating
from movie_rating_system.movie import Movie
from unittest import TestCase

class TestMovieRatingApp(TestCase):

    def test_that_movie_list_isEmpty(self):
        movi = Movie(self)
        self.assertEqual(movi.movie_list(), [])

    def test_that_rating_list_isEmpty(self):
        rate = Rating()
        self.assertEqual(rate.rating_list(), [])

    def test_that_movie_can_be_added(self):
        movi = Movie(self)
        movi.add_movie("Semicolon")
        self.assertEqual([{'name': 'Semicolon', 'date': '06 07 2025  9:35 AM'}], movi.movie_list())

    def test_that_rating_list_can_be_added(self):
        rate = Rating()
        movi = Movie(self)
        movi.add_movie("Semicolon")
        rate.add_rating_list([])
        self.assertEqual([[]], rate.rating_list())

    def test_that_movie_can_be_removed(self):
        movi = Movie(self)
        movi.add_movie("Semicolon")
        rate = Rating()
        rate.add_rating_list([])
        movi.remove_movie("Semicolon")

        self.assertEqual([], rate.rating_list())
