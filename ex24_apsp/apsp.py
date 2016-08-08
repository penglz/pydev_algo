#Floyd-Warshall algorithm
import numpy as np
import sys

def fw_apsp(lines):
    minp = 2**31-1
    n,m = map(int, lines[0].split())
    A = np.full((2, n, n), minp,dtype=np.int32)
    for i in range(n):
        A[0, i, i] = 0

                    
    for line in lines[1:]:
        u, v, c = map(int, line.split())
        A[0, u - 1, v - 1] = c
            
    s = 0
    for k in range(n):
        s = 1 - s
        for i in range(n):
            for j in range(n):
                A[s,i,j] = min(A[1-s,i,j], A[1-s,i,k]+A[1-s,k,j])
                if A[s,i,j] < minp:
                    minp = A[s,i,j]
                
    for i in range(n):    
        if A[s,i,i] < 0:
            print 'Has negative cost cycle'
            return 
    
    print 'Has shortest path', minp          

def main():


    print 'Loading P1...'
    with open('./g1.txt', 'r') as f:
        lines = f.readlines()
        fw_apsp(lines)
        
    print 'Loading P2...'
    with open('./g2.txt', 'r') as f:
        lines = f.readlines()
        fw_apsp(lines)
        
    print 'Loading P3...'
    with open('./g3.txt', 'r') as f:
        lines = f.readlines()
        fw_apsp(lines)





if __name__ == "__main__":
    main()
