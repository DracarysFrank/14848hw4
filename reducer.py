#!/usr/bin/env python

from operator import itemgetter
import sys

curr_date = None
max_temp = -float('inf')

# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    date, temp = line.split('\t', 1)
    # convert count (currently a string) to int
    temp = int(temp)

    if date == curr_date:
        max_temp = max(max_temp, temp)
    else:
        if curr_date is not None:
            print('%s\t%s' % (curr_date, max_temp))
        curr_date = date
        max_temp = temp

if max_temp != -float('inf'):
    print('%s\t%s' % (curr_date, max_temp))
