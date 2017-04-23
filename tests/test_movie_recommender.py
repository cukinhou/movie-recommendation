import json
import numpy as np
import pandas as pd

from unittest import TestCase
from movierec.movie_recommender import MovieRecommender


class TestMovieRecommender(TestCase):

    DEFAULT_DATA_PATH = 'movies_data/movies.json'

    @classmethod
    def setUpClass(cls, path=DEFAULT_DATA_PATH):
            cls.data = json.load(open(path, 'rb'))
            cls.recommender = MovieRecommender(cls.data)

    def test_compute_svd(self):
        test_m = np.random.random([10, 10])
        test_m_rec = self.recommender.compute_svd(test_m)

        expected = True
        got = np.allclose(test_m, test_m_rec)

        self.assertEquals(got, expected)

    def test_get_movie_title(self):
        test_mid = 55

        expected = 'Top Gun (1986)'
        got = self.recommender.get_movie_title(test_mid)

        self.assertEquals(got, expected)

    def test_get_movie_titles(self):
        test_mids = [1, 55]

        expected = ['Toy Story (1995)', 'Top Gun (1986)']
        got = self.recommender.get_movie_titles(test_mids)

        np.testing.assert_array_equal(got, expected)

    def test_apply_format_data(self):
        data = np.random.random([10, 1])

        expected = np.add(data, 1)
        got = self.recommender._apply_format_data(
            data, lambda x: np.add(x, 1), 0
        )

        np.testing.assert_array_equal(got, expected)

    def test_get_rating_vector(self):
        movie_ids = [10, 12, 16, 40]
        expected_movies = np.zeros(self.recommender.n_movies)
        expected_movies[np.subtract(movie_ids, 1)] = 1

        got_movies = self.recommender._get_rating_vector(movie_ids)
        np.testing.assert_equal(got_movies, expected_movies)

    def test_select_n_best_movies(self):
        p_ratings = pd.Series(range(0, 10))

        expected = 9
        got = self.recommender.select_n_best_movies(p_ratings, n=1)

        self.assertEquals(got, expected)

    def test_add_user(self):
        test_mids = [1, 2, 5, 10]

        got_uid = self.recommender.add_user(test_mids)
        expected_uid = self.recommender.n_users

        self.assertEquals(got_uid, expected_uid)
