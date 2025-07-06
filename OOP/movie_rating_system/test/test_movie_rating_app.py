from movie_rating_system.movie import Movie
from unittest import TestCase

class TestMovieRatingApp(TestCase):

    def test_(self):
        move = Movie(self)
        self.assertEqual(move.movie_list(), [])