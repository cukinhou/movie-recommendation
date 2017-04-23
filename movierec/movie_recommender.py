"""
This class implements a simple movie recommendation system
based on Singular Value Decomposition (SVD). A matrix 'M'
with values 1 (seen) and 0 (not seen), as a way of rating,
is created out of the input data. This matrix is factorize
and reconstructed using SVD. This method allows to reduce
the influence of noise and enhacie popular trends in the data.

author: Javier Nistal
"""
import numpy as np
import pandas as pd


class MovieRecommender(object):
    def __init__(self, data):
        """
        Extracts and formats the users and movies data

        :type data: dict
        :param data: movie/user info
        """
        assert 'movies' and 'users' in data.keys(), \
            'Input data does not follow the expected structure: ' \
            'data = dict{"movies": [{movie_ids: movie_name}], "users": [{}]}'

        self.n_movies = len(data['movies'])
        self.n_users = len(data['users'])

        self.movies = pd.Series(data['movies'])
        self.usr_info = pd.Series(
            data['users'], index=range(1, self.n_users+1)
        )

        self.ratings = self._apply_format_data(
            self.usr_info, self._get_rating_vector
        ).T
        print 'recommender created'


    @staticmethod
    def compute_svd(m):
        """
        Computes Singular Value Decomposition (SVD) of the input matrix.

        :type m: array_array
        :param m: input matrix

        :rtype m_rec: pandas.DataFrame
        :return m_rec: reconstructed matrix.
        """
        U, s, V = np.linalg.svd(m, full_matrices=False)
        m_rec = np.dot(U, np.dot(np.diag(s), V))
        return m_rec

    def get_movie_title(self, mid):
        """
        Returns the name of a movie identified by its ID

        :type mid: Int
        :param mid: movie ID

        :returns m_name: name of the movie
        """
        return self.movies[str(mid)]

    def get_movie_titles(self, mids):
        """
        Returns the titles of a set of movies

        :type mids: list_ints
        :param mids: movie IDs

        :returns: movie titles
        """
        return pd.Series(map(
            lambda x: self.get_movie_title(x), mids
        ), index=range(1, len(mids) + 1))

    def _apply_format_data(self, data, f, field='movies'):
        """
        Applies function 'f' on each element of 'field' in data

        :type data: array_dict
        :param data: input data

        :type f: function
        :param f: method to apply to each item

        :type field: str
        :param field: field of data

        :rtype: pandas.Dataframe
        :returns: formatted data
        """
        return pd.DataFrame(
            data=map(
                lambda x: f(x[field]), data
            ), index=range(1, data.shape[0] + 1)
        )

    def _get_rating_vector(self, mids):
        """
        Sets to '1' (rating) the movies seen by a certain user

        :type mids: list_int
        :param mids: movie IDs

        :rtype ratings: pandas.Series
        :return ratings: movie ratings (1/0)
        """
        ratings = pd.Series(index=range(1, self.n_movies + 1)).fillna(0)
        ratings[mids] = 1
        return ratings

    def select_n_best_movies(self, p_ratings, n=10):
        """
        Selects the n best rated movies from the prediction

        :type p_ratings: pandas.Series
        :param p_ratings: predicted ratings

        :type n: int
        :param n: number of output movies

        :returns: n sorted predicted ratings
        """
        return p_ratings.sort_values(ascending=False)[0:n].index

    def add_user(self, mids):
        """
        Adds a new user and its ratings.

        :type mids: list_int
        :param mids: IDs of movies watched by user

        :rtype uid: int
        :return uid: user identifier
        """
        self.n_users += 1
        uid = self.n_users

        self.ratings[uid] = self._get_rating_vector(mids)
        self.usr_info[uid] = mids
        return uid

    def recommend(self, mids):
        """
        Executes the algorithm and provides recommendation for a given
        input movie query.

        :type mids: list_int
        :param mids: movie IDs

        :rtype: pandas.Series_str
        :returns: recommended movie titles
        """
        uid = self.add_user(mids)
        m = self.ratings.copy()
        m_rec = self.compute_svd(m)
        m_rec = pd.DataFrame(m_rec, index=m.index, columns=m.columns)

        p_ratings = m_rec[uid]
        p_ratings[mids] = 0
        best_rec = self.select_n_best_movies(p_ratings)

        return self.get_movie_titles(best_rec)
