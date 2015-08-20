# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:46:39 2015

@author: emg
"""

import cPickle as pickle
import scipy as sp
from tools import pickle_dump, pickle_load

'''Editing, dumping, and loading ratings_list'''
ratings_file = 'ratings.list'

def read_ratings(filename, header=281407, footer=633534):
    '''creates dict of film names : rating from ratings_file'''
    results = {}
    for i, line in enumerate(open(filename)):
        if header < i <= footer:       
            name = line.split('  ')[-1].strip()
            rating = line.split('  ')[-2].strip()
            results[name] = rating
            #if i%1000 == 0:
                #print i, 'rating', rating, name
    return results

def dump_ratings_list():
    ratings_list = read_ratings(ratings_file)
    pickle_dump(ratings_list)

ratings_list = pickle_load('ratings_list')

def get_ratings(name, filmography_dict):
    '''get the ratings for every film by the writer of director
    filmography_dict = director_films or writer_films'''
    ratings = []
    nums = []
    films = filmography_dict[name]
    for film in films:
        if film in set(ratings_list):
            rating = float(ratings_list[film])
        else:
            rating = sp.nan # figure out why some ratings not found
        ratings.append([film, rating])
        nums.append(rating)
    ratings.append(['Average Rating', sp.nanmean(nums)])
    return ratings

def avg_rating(name, filmography_dict):
    ''''returns avg rating of a writer or director'''
    ratings = get_ratings(name, filmography_dict)
    avg = ratings[-1][1]
    return avg

# is this the best way to create dicts w/ ratings?
def add_ratings(filmography_dict):
    for name, films in filmography_dict.iteritems():
        new = []
        nums = []
        for film in films:
            if str(film) in set(ratings_list):
                rating = ratings_list[film]
            else:
                rating = sp.nan
                new.append([film, rating])
            nums.append(rating)
        new.append(['Average Rating', sp.nanmean(nums)])
        filmography_dict[name] = new
    return filmography_dict