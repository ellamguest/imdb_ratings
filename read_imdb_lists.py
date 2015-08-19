# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:42:04 2015

@author: emg
"""
from itertools import dropwhile, takewhile, islice

actors_file = 'actors.list'
actresses_file = 'actresses.list'
directors_file = 'directors.list'
writers_file = 'writers.list'
ratings_file = 'ratings.list'

#find better way of determining header/footers?

def get_director_lines(filename, header=234, footer=2639293):
    '''creates list of lines from directors_file'''
    results = []
    for i, line in enumerate(open(filename)):
        if header < i <= footer:
            results.append(line)
            if i%1000 == 0:
                print i, 'director', line
    return results

def get_writer_lines(filename, header=301, footer=4101660):
    '''creates list of lines from writers_file'''
    results = []
    for i, line in enumerate(open(filename)):
        if header < i <= footer:        
            results.append(line)
            if i%1000 == 0:
                print i, 'writer', line
    return results

##### AM I USING THESE?

def get_line_index(line, filename):
    """determining the index of a line in a file
        useful for headers and footers"""
    for x in list(enumerate(open(filename))):
        if x[1] == line:
            i = x[0]
            return i

def get_bookend_indices(header, footer, filename):
    h_i = get_line_index(header, filename)
    f_i = get_line_index(footer, filename)
    return h_i, f_i

#working on...

def get_actor_lines():
    header = '----\t\t\t------'
    footer = str('-'*77)
    filename = 'actors.list'
    indices = get_bookend_indices(header, footer, filename)
    results = []
    for i, line in enumerate(open(filename)):
        if indices[0] < i <= indices[1]:
            results.append(line)
            if i%10000 == 0:
                print i, 'actor', line
    return results

def get_actor_lines2():
    header = '----\t\t\t------'
    footer = str('-'*77)
    filename = 'actors.list'
    results = []
    marker_reached = False
    for i, line in enumerate(open(filename)):
        if line == header:
            marker_reached = True
        elif line == footer:
            marker_reached = False
        elif marker_reached:
            results.append(line)
    return results

#andy recommends itertools...
    
def get_actress_lines():
    return

