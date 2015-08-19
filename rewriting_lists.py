# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:21:31 2015

@author: emg
"""

from itertools import dropwhile, takewhile, islice
from line_processing import pull_items
from tools import rewrite_file

actors_file = 'actors.list'
actresses_file = 'actresses.list'
directors_file = 'directors.list'
writers_file = 'writers.list'
ratings_file = 'ratings.list'

def get_body(filename, header='----\t\t\t------', footer='-'*77 ):
    fp = open(filename)
    at_header = dropwhile(lambda l: l.strip() != header, fp)
    after_header = islice(at_header, 1, None)
    until_footer = takewhile(lambda l: l.strip() != footer, after_header)
    return list(until_footer)

def write_body_file(filename, **kwargs):
    body = get_body(filename, **kwargs)
    name = '{0}.txt'.format(filename[:-5])
    new = open(name, 'w+')
    new.writelines(body)
    new.close()
    
ratings_list = read_ratings(ratings_file)

def edit_ratings_file():
    '''reduces lines to name : rating'''
    write_body_file('ratings.list', header='!New  Distribution  Votes  Rank  Title', footer='-'*78) #creates ratings.txt    
    fp = open('ratings.txt', 'r+')
    results = []
    for line in fp:
        name = line.split('  ')[-1].strip()
        rating = line.split('  ')[-2].strip()
        info = '{0} : {1}\n'.format(name, rating)
        print info
        results.append(info)
        line
    return results
    """fp.seek(0)
    fp.writelines(results)
    fp.close()"""
    
edit_ratings_file()
    

''' TO INTIALLY WRITE THE FILES:
write_body_file('actors.list') #creates actors.txt
write_body_file('actresses.list') #creates actresses.txt
write_body_file('directors.list') #creates directors.txt
write_body_file('writers.list', footer='-'*69) #creates writers.txt

'''

def write_filmography_file(filename):
    fp = open(filename, 'w')    
    print 'pulling items...'''
    info = pull_items(filename)
    fp.close()
    fp = open(filename, 'w+')   
    print 'rewriting file...'
    rewrite_file(filename, info)

#write_filmography_file('directors.') #creates directors.txt