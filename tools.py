# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:07:29 2015

@author: emg
"""

import cPickle as pickle

def pickle_dump(info, name):
    '''Dump info into file info.pickle'''
    pickle.dump(info, open('{0}.pickle'.format(name), 'w+'))
    
def pickle_load(name):
    '''Load info from file info.pickle'''
    return pickle.load(open('{0}.pickle'.format(name), 'r')) 

def dict_to_list(d):
    '''converts d to l in format [[k,v,v],[k2,v2,2]'''
    l = []
    for k, vs in d.iteritems():
        line = [k]
        for v in vs:
            line.append(v)
        l.append(line)
    return l

def rewrite_file(fp, info):
    '''fp should already = open(filename, 'r+')'''
    fp.seek(0)
    fp.writelines(info)
    fp.close()

def write_dict_name(d):
    """adds _dict to actor, actress, director or writer"""
    if d in ['actor', 'actress', 'director', 'writer']:
        name = '{0}_dict'.format(d)
        return name
    else:
        print 'Not a valid dictionary'

def check_in_dict(name, d):
    """name should be in last, first format"""
    d = write_dict_name(d)
    if d == 'Not a valid dictionary':
        print d
    else:
        return [n for n in d if name.title() in n]

def make_reverse_dict(d):
    '''reverse any dict, accounting for possible multiple values'''
    results = {}
    for k, vs in d.iteritems():
        for v in vs:
            results[v] = results.get(v, []) + [k]
    return results

def frequency_dict(names):
    """make dict of # : names"""
    d = {}
    for name in names:
        d[str(name)] = d.get(str(name), 0) + 1
    result = make_reverse_dict({k: [v] for k, v in d.iteritems()})
    return result

def most_popular(names):
    """makes a ranked list from the frequency_dict"""
    d = frequency_dict(names)
    p = []
    for k, v in d.iteritems():
        n = [k]
        for x in v:
            n.append(x)
        p.append(n)
    p.sort(reverse=True)
    return p

def get_film_info(film):
    '''get the film's [rating, director, writer]'''
    rating = ratings_list[film]
    director = film_directors[film]
    writer = film_writers[film]
    return [rating, director, writer]

def films_info_dict(films):
    '''make a dict of film : [ratings, director, writer] for films in list'''
    d = {}
    for film in films:
        d[film] = get_film_info(film)
    return d