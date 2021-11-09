#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import sys

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    try:
        temp = int(line[87:92])
    except ValueError:
        continue
    quality = line[92]
    if temp == 9999 or quality not in {'0', '1', '4', '5', '9'}:
        continue

    date = line[15:23]
    print('%s\t%s' % (date, temp))
