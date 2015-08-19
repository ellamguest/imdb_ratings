# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:46:39 2015

@author: emg
"""

import cPickle as pickle

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

ratings_list = read_ratings(ratings_file)

def save_film_ratings():
    ratings_list = read_ratings(ratings_file)
    pickle.dump(ratings_list, open('ratings_list.pickle', 'w+'))

save_film_ratings()

def load_ratings_list():    
    return pickle.load(open('ratings_list.pickle', 'r'))

ratings_list = load_ratings_list()



