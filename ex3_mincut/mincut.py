from random import seed, randint
from copy import deepcopy
from math import log

def find_root(cuts, i):
    if cuts[i] != i:
        cuts[i] = find_root(cuts, cuts[i])
    return cuts[i]
    

def contract(vertexs, edges, cuts, e):
    while True:
        u,v = edges[e]
        u = find_root(cuts, u)
        v = find_root(cuts, v)
        if (u != v):
            break
        e = randint(0, len(edges)-1)
    
    
    if len(vertexs.get(u, [])) > len(vertexs.get(v, [])):
        w = u
    else:
        w = v
        v = u

    
    cuts[v] = w    

    #print e, v, cuts[v]
        
        
        
def karger_min_cut(vertexs, edges):
    n = max(vertexs.keys())
    cuts = range(n+1)
    
    for _ in xrange(n-2):
        edges_index = randint(0, len(edges)-1)
        contract(vertexs, edges, cuts, edges_index)
        #print G, edges

    #assert(len(vertexs) == 2)
    #u = vertexs.keys()[0]
    #assert(len(vertexs[u]) == len(vertexs[v]))

    #before returning the cuts list, we must remove the self loops from the adjacency list 
    #return filter(lambda (k, z): cuts[z] != cuts[k], vertexs[u])  
    return filter(lambda (k, z): (find_root(cuts,z) != find_root(cuts,k)) and (k < z), edges)
    

def main():
    vertexs = {}
    edges = []
    with open('./kargerMinCut.txt', 'r') as f:
        for line in f:
            vals = map(int, line.split())
            v = vals[0]
            vertexs[v] = map(lambda u: (v,u), vals[1:])
            for i in xrange(1, len(vals)):
                edges.append((v, vals[i]))
    
    n = len(vertexs)
    N = int(n*n)
    min_cut_len = float('inf')
    min_cut = []       
    seed()
    for _ in xrange(N):       
        v_1 = deepcopy(vertexs)
        
        mc = karger_min_cut(v_1, edges)
        if len(mc) < min_cut_len:
            min_cut_len = len(mc)
            min_cut = mc
            print min_cut

    print min_cut_len

    #iarray = [1, 2, 3, 4, 5, 6, 7, 8]




if __name__ == "__main__":
    main()
