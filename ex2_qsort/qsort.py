#! /usr/bin/env python
##!/usr/bin/python
########! /usr/bin/env python

def choose_pivot(iarray, lo, hi, method):
    if method == 1:
        return lo 
    elif method == 2:
        return hi
    elif method == 3:
        idx = (lo + hi) // 2 
        if iarray[lo] < iarray[hi]:
            if iarray[idx] < iarray[lo]:
                return lo
            elif iarray[idx] > iarray[hi]:
                return hi
            else:
                return idx
        else:
            if iarray[idx] < iarray[hi]:
                return hi
            elif iarray[idx] > iarray[lo]:
                return lo
            else:
                return idx
        

def partion(iarray, lo, hi, pivot):
    pv = iarray[pivot]
    if (pivot != lo):
        iarray[lo],iarray[pivot] = iarray[pivot],iarray[lo]
    i = lo + 1 
    j = lo + 1
    while j < hi+1:
        if (iarray[j] < pv):
            if (j != i):
                iarray[i],iarray[j] = iarray[j],iarray[i]
            i += 1
        j += 1
    if (i-1) != lo :
        iarray[lo], iarray[i-1] = iarray[i-1], iarray[lo]
    return i-1
            


def myqsort(iarray, lo, hi, method, ncomp):
    if (lo == hi):
        return ncomp 
    else:
        ncomp = ncomp + (hi - lo)
        p = choose_pivot(iarray, lo, hi, method)
        p = partion(iarray, lo, hi, p)
        if (p > lo):
            ncomp = myqsort(iarray, lo, p-1, method, ncomp)
        if (p < hi-1):
            ncomp = myqsort(iarray, p+1, hi, method, ncomp)
        return ncomp


def main():
    with open('./QuickSort.txt', 'r') as f:
        iarray = map(int, f.readlines())
    #iarray = [1, 2, 3, 4, 5, 6, 7, 8]
    iarray_ans = sorted(iarray)
    
    iarray_work = list(iarray)    
    ncomp = myqsort(iarray_work, 0, len(iarray)-1, 1, 0)
    if iarray_ans == iarray_work:
        print ncomp
    else:
        print 'Wrong Answer'
     
    iarray_work = list(iarray)
    ncomp = myqsort(iarray_work, 0, len(iarray)-1, 2, 0)
    if iarray_ans == iarray_work:
        print ncomp
    else:
        print 'Wrong Answer'
         
    iarray_work = list(iarray)    
    ncomp = myqsort(iarray_work, 0, len(iarray)-1, 3, 0)
    if iarray_ans == iarray_work:
        print ncomp
    else:
        print 'Wrong Answer'



if __name__ == "__main__":
    main()
