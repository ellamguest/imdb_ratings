# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:09:05 2015

@author: emg
"""

from tools import pickle_load, make_reverse_dict

writer_films = pickle_load('writers_file')
film_writers = make_reverse_dict(writer_films)

director_films = pickle_load('directors_file')
film_directors = make_reverse_dict(director_films)

actress_films = pickle_load('actresses_file')
film_actresses = make_reverse_dict(actress_films)

