#! /usr/bin/env python
##!/usr/bin/python
########! /usr/bin/env python
from collections import defaultdict



def main():
    
    with open('./2sum.txt', 'r') as f:
        iarray = map(int, f.readlines())

    myset = set(iarray)
    iarray = sorted(myset)  
 
    i = 0
    j = len(iarray) - 1
    lasti = i
    lastj = j
    
    myhash = {}
    while i < j:
        t = iarray[i] + iarray[j]
        if t > 10000:
            lastj = j
            j -= 1
        elif t < -10000:
            lasti = i
            i += 1
            j = lastj 
        else:
            myhash[t] = True 
            if j < lastj:
                j -= 1
            else:
                i += 1
            


                   
    print len(myhash.keys())

    #iarray = [1, 2, 3, 4, 5, 6, 7, 8]




if __name__ == "__main__":
    main()
