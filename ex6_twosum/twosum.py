#! /usr/bin/env python
##!/usr/bin/python
########! /usr/bin/env python
from collections import defaultdict



def main():
    
    with open('./2sum.txt', 'r') as f:
        iarray = map(int, f.readlines())

    myset = frozenset(iarray)  
    mysum = 0
 
    for t in range(-10000,10001):
        for x in myset:
            if t - x in myset and t - x != x:
                mysum += 1
                break
        if t%1000==0:
            print t, 'done'

                   
    print mysum

    #iarray = [1, 2, 3, 4, 5, 6, 7, 8]




if __name__ == "__main__":
    main()
