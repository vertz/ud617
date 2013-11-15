#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split()

    if len(data) < 8:
        continue

    # ip, id, username
    h, l, u = data[:3]

    t = data[3:5]
    # parse time [%t]
    t[0] = t[0][1:]
    t[1] = t[1][:-1]

    # parse request \"%r\"
    r = data[5: -2]
    if len(r) > 1:
        r[ 0] = r[0][1:]
        r[-1] = r[-1][:-1]
        
    # status code, size
    s = data[-2]
    b = data[-1]

    if len(r) == 3:
        print "{0}\t{1}".format(h, 1)
    
