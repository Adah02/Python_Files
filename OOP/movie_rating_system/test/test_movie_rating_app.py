from movie_rating_system.movie_rating import Movie
from unittest import TestCase

class TestMovieRatingApp(TestCase):

    def test_that_movie_list_isEmpty(self):
        movi = Movie()
        self.assertEqual(movi.movie_list(), [])

    def test_that_rating_list_isEmpty(self):
        movi = Movie()
        self.assertEqual(movi.rating_list(), [])

    def test_that_movie_is_added(self):
        movi = Movie()
        movi.add_movie("Semicolon")
        self.assertEqual([{'date': '15 07 2025  11:08 PM', 'name': 'Semicolon'}], movi.movie_list())

    def test_that_rating_list_is_added(self):
        movi = Movie()
        movi.add_movie("Semicolon")
        self.assertEqual([[]], movi.rating_list())

    def test_that_movie_can_be_removed(self):
        movi = Movie()
        movi.add_movie("Semicolon")
        self.assertEqual([[]], movi.rating_list())
        movi.remove_movie("Semicolon")
        self.assertEqual([], movi.rating_list())