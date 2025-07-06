from contextlib import nullcontext

from movie_rating_system.movie import Movie
from unittest import TestCase

class TestMovieRatingApp(TestCase):

    def test_(self):
        self.assertEqual(Movie.movie_list(self = nullcontext ), [])


