#!/usr/bin/python

# __author__ = 'rfischer'
import math

T = int(raw_input())

m = [0]
s = 1
c = 1
while s <= 2*(10**9):
    m.append(s);
    c += 1;
    s = c * c
    #print "new square is: " + str(s)
#print "last square was " + str(s)
lm = len(m)
#print "m: ",
#print m,
#print ", lm: " + str(lm)
z = 0

for t in range(0, T):
    d, k = [int(x) for x in raw_input().split(' ')]
    #print "d: " + str(d) + ", k: " + str(k)

    x = 0
    edge_cities = 0
    diff = d - m[x]
    while x < lm and m[x] < d: # and diff >= m[x]:
        #print "x: " + str(x) + ", diff: " + str(diff)
        #if diff == 0:
        #    edge_cities += 1
            #print "City found at x: " + str(x) + ", 0"
        #else:
        # see if d - m[x] equals any of the squares
        #y = 0
        #while y < lm and m[y] <= diff:
        #    if m[y] == diff:
        #        edge_cities += 1
                #print "City found at x: " + str(x) + ", y: " + str(y)
         #   y += 1
        y = float(math.sqrt(diff))
        if y == math.floor(y):
            #print "City found at x: " + str(x + 1) + ", y: " + str(int(y))
            edge_cities += 1

        x += 1
        if x < lm:
           diff = d - m[x]

    # *8 because only looking at 1/2 quadrant.  -4 because there are always 4 at each axis
    if (edge_cities * 4 <= k):
        print "possible"
    else:
        print "impossible"
        #print "For d: " + str(d) + " quadrant cities were: " + str(edge_cities + 1)



