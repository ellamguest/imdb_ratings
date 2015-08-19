# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:21:31 2015

@author: emg
"""

from itertools import dropwhile, takewhile, islice
from line_processing import pull_items
from tools import rewrite_file, pickle_dump, pickle_load

actors_file = 'actors.list'
actresses_file = 'actresses.list'
directors_file = 'directors.list'
writers_file = 'writers.list'

def dump_body(filename, header='----\t\t\t------', footer='-'*77 ):
    fp = open(filename)
    at_header = dropwhile(lambda l: l.strip() != header, fp)
    after_header = islice(at_header, 1, None)
    until_footer = takewhile(lambda l: l.strip() != footer, after_header)
    pickle_dump(list(until_footer))

dump_body(writers_file)

'''def write_body_file(filename, **kwargs):
    body = get_body(filename, **kwargs)
    name = '{0}.txt'.format(filename[:-5])
    new = open(name, 'w+')
    new.writelines(body)
    new.close()

test = get_body(writers_file)

def write_filmography_file(filename):
    fp = open(filename, 'w')    
    print 'pulling items...'
    info = pull_items(filename)
    fp.close()
    fp = open(filename, 'w+')   
    print 'rewriting file...'
    rewrite_file(filename, info)'''

#write_filmography_file('directors.') #creates directors.txt