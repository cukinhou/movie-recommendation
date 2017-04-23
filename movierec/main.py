#!/usr/bin/env python
"""
Main function for executing 'movie_recommender.py'
author: Javier Nistal
"""
import argparse
import json

from movie_recommender import MovieRecommender

def main(args):
    user_pref = args.user_pref
    data_path = args.data_path
    data = json.load(open(data_path, 'rb'))

    assert True in [i <= 70 for i in user_pref], \
        'We currently have up to 70 movies! Choose a set of movie ' \
        'IDs in the range [1-70].'

    recommender = MovieRecommender(data)
    recommendation = recommender.recommend(user_pref)
    print 'hola'
    liked_movies = recommender.get_movie_titles(user_pref)

    print 'You liked:\n {0} \n\n We recommend you: \n{1}'.format(
        liked_movies, recommendation
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Movie recommender')

    parser.add_argument(
        '-u',
        dest='user_pref',
        nargs='+',
        type=int,
        required=True,
        help='Input: vector containing the movie IDs you like. Example: \
        "-u 3 5 8 53 60"'
    )
    parser.add_argument(
        '-p',
        dest='data_path',
        default='movies_data/movies.json',
        help='Input: path to JSON file containing user profiles. \
        DEFAULT: moies_data/movies.json'
    )
    args = parser.parse_args()

    main(args)
