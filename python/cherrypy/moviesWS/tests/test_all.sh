#!/bin/bash

printf "testing /movies/\n"
python2.6 test_movies_index.py

printf "\ntesting /movies/:movie_id\n"
python2.6 test_movies.py

printf "\ntesting /ratings/:movie_id\n"
python2.6 test_ratings.py

printf "\ntesting /recommendations/\n"
python2.6 test_recommendations_index.py

printf "\ntesting /recommendations/:user_id\n"
python2.6 test_recommendations.py

printf "\ntesting /users/\n"
python2.6 test_users_index.py

printf "\ntesting /users/:users_id\n"
python2.6 test_users.py

