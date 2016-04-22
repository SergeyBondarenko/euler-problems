#!/usr/bin/python

n = 0
MAX = 999
MIN = 99

for i in xrange(MAX, MIN, -1):
    for j in xrange(i, MIN, -1):
        if i * j > n:
            s = str(i * j)
            if s == s[::-1]:
                n = i * j

print n
