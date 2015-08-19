# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:46:39 2015

@author: emg
"""

import cPickle as pickle
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



