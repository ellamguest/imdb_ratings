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

# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:42:04 2015

@author: emg
"""

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


