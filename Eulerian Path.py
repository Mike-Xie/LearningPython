#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Mike
#
# Created:     24/10/2013
# Copyright:   (c) Mike 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a = [(1, 2), (2, 3), (3, 1)]

b = [(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]

c = [(1, 13), (1, 6), (6, 11), (3, 13),
(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
(1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
(7, 14),  (10, 13)]

d = [(8, 16), (8, 18), (16, 17), (18, 19),
(3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]

def findtour(graph):
    copy = graph # don't want to modify the existing graph in case something bad happens

    tour = []

    def connected(aNode):

        for (i,j) in copy:
            if aNode == i:
                print (i,j)
                copy.remove((i,j))
                connected(j)
            if aNode == j:
                print (i,j)
                copy.remove((i,j))
                connected(i)
        tour.append((aNode))

    connected(copy[0][0])
    tour.reverse()
    return tour

print findtour(a)

