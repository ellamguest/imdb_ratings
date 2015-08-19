# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:01:38 2015

@author: emg
"""

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