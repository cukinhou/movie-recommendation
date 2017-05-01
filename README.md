===========
Movie Rec
===========

Movie Rec provides movie recommendation based on
Singular Value Decomposition (SVD). Given a set of
SVD fills unrated movies based on the ratings of 
other users. Usage::

    cd [path]/MovieRecommender

    python movierec/main.py -u [movie_IDs] -p [path_to_json_file]

    Example:

    python movierec/main.py -u 3 10 50 63 -p movies_data/movies.json


(Note: argument '-p' is by default 'movies_data/movies.json')

If movirec used as a package:

    import json
    from movierec.movie_recommender import MovieRecommender

    user_pref = [movie_ID1, movie_ID2, ..., movie_IDn]
    path = 'some_path/movies.json'
    data = json.load(open(path, 'rb'))

    recommendation = MovieRecommender(data).recommend(user_pref)


Install
=========

Run the following commands from movierec root folder:

* easy_install pip (only if you don't have pip installed)

* make init

For installing movierec package:

* make install

Running tests:
-------------

* pip install nose (if you don't have installed nose)

* make test
