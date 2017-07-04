# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:03:16 2016

@author: emg
"""

import pandas as pd
from line_processing import *
from read_film_files import get_director_lines


# make list of lines from data
lines = get_director_lines('/Users/emg/Programmming/GitHub/imdb_ratings/imdb_redo/directors.list', header=234, footer=2639293)

# make dict of directors:credits
d = pull_items(lines)

# make list of directors + all credits
c = list()
for x in d:
    c.append([x, d[x]])
         
# make list of individual director credits
n = list()
for i in range(len(c)):   
    for q in range(len(c[i][1])):
        n.append([c[i][0], c[i][1][q]])

# convert to df
df = pd.DataFrame(n)
df.columns = ['name', 'credit']

 # save basic df
df.to_csv('basic_director_credits')

# open basic file
df = pd.read_csv('basic_director_credits')

# edit columns
df['last'], df['first'] = df['name'].str.split(', ', 1).str
df['credit_name'], df['year'] = df['credit'].str.split(' \(', 1).str
df['year'] = df['year'].map(lambda x: x.rstrip('\)'))
df['credit'] = df['credit_name']
df = df[['last','first','credit', 'year']]

df.to_csv('director_credits')
