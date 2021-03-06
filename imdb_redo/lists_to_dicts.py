# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:21:31 2015

@author: emg
"""

from itertools import dropwhile, takewhile, islice
from line_processing import pull_items
from tools import rewrite_file, pickle_dump, pickle_load
import pdb

actors_file = 'actors.list'
actresses_file = 'actresses.list'
directors_file = 'directors.list'
writers_file = 'writers.list'

def dump_body(filename, name, header='----\t\t\t------', footer='-'*77 ):
    fp = open(filename)
    at_header = dropwhile(lambda l: l.strip() != header, fp)
    after_header = islice(at_header, 1, None)
    until_footer = takewhile(lambda l: l.strip() != footer, after_header)
    pdb.set_trace()
    info = list(until_footer)
    pickle_dump(info, name)
    pdb.set_trace()
    
'''WOULD COMBINING THESE BE MORE OR LESS EFFICIENT?'''    

def dump_pulled_dict(name):
    pdb.set_trace()
    raw_data = pickle_load(name)
    pdb.set_trace()
    info = pull_items(raw_data)
    pdb.set_trace()
    pickle_dump(info, name)
    pdb.set_trace()

'''INITIALZING WRITERS_DICT
dump_body(writers_file, 'writers_file', footer='-'*69)
dump_pulled_dict('writers_file')
writers_dict = pickle_load('writers_file')'''

'''INITIALIZING DIRECTORS_DICT
dump_body(directors_file, 'directors_file')
dump_pulled_dict('directors_file')
directors_dict = pickle_load('directors_file')'''

'''INITIALIZING ACTRESSES_DICT
dump_body(actresses_file, 'actresses_file')
dump_pulled_dict('actresses_file')
actresses_dict = pickle_load('actresses_file')'''
#dump_body(actors_file, 'actors_file')
#dump_pulled_dict('actors_file')
actors_dict = pickle_load('actors_file')