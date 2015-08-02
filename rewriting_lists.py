# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:21:31 2015

@author: emg
"""

from itertools import dropwhile, takewhile, islice
from line_processing import pull_items
from tools import rewrite_file


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
    
def edit_ratings_file():
    '''reduces lines to name : rating'''
    write_body_file('ratings.list', header='!New  Distribution  Votes  Rank  Title', footer='-'*78) #creates ratings.txt    
    fp = open('ratings.txt', 'r+')
    results = []
    for line in fp:
        name = line.split('  ')[-1].strip()
        rating = line.split('  ')[-2].strip()
        info = '{0} : {1}\n'.format(name, rating)
        results.append(info)
        line
    fp.seek(0)
    fp.writelines(results)
    fp.close()
    
#edit_ratings_file()
    

''' TO INTIALLY WRITE THE FILES:
write_body_file('actors.list') #creates actors.txt
write_body_file('actresses.list') #creates actresses.txt
write_body_file('writers.list', footer='-'*69) #creates writers.txt

'''
def get_director_lines(filename, header=234, footer=2639293):
    '''creates list of lines from directors_file'''
    results = []
    for i, line in enumerate(open(filename)):
        if header < i <= footer:
            results.append(line)
            if i%1000 == 0:
                print i, 'director', line
    return results



#write_body_file('directors.list') 



def write_filmography_file(filename):
    print 'pulling items...'''
    info = pull_items(filename)
    print 'rewriting file...'
    rewrite_file(filename, info)

write_filmography_file('directors.list') #creates directors.txt