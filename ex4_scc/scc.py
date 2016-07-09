from collections import defaultdict
import sys

def DFS(G, i, s, f, visited, scc):
    mystack = []
    mystack.append(i)
    visited[i] = 1
    scc[s] = scc[s] + 1
    while mystack:
        ii = mystack[-1]
        allvisited = True
        #print ii, G[ii]
        for j in G[ii]:
            if not visited[j]:
                visited[j] = 1
                scc[s] = scc[s] + 1
                mystack.append(j)
                allvisited = False
        if not G[ii] or allvisited:
            f.append(ii)
            mystack.pop()

            
def SCC(G, G_r, n):    
    s = -1
    visited = [0] * n
    scc = [0] * n
    f = []
    for i in G_r.keys():
        if (not visited[i]):
            s = i
            DFS(G_r, i, s, f, visited, scc)
            
    s = -1
    scc = [0] * n
    f_ = []
    visited = [0] * n
    n = len(f)
    for _ in xrange(n):
        i = f.pop()
        if (not visited[i]):
            s = i
            DFS(G, i, s, f_, visited, scc)
            
    return scc
    

def main():

    vertexs = defaultdict(list)
    vertexs_r = defaultdict(list)

    max_u = -1
    with open('./SCC.txt', 'r') as f:
        for line in f:
            vals = map(int, line.split())
            u = vals[0] - 1
            v = vals[1] - 1
            if (u > max_u):
                max_u = u 
            if (v > max_u):
                max_u = v
            vertexs[u].append(v)
            vertexs_r[v].append(u)
          
    print len(vertexs), len(vertexs_r)
    max_u = max_u + 1
    # sys.setrecursionlimit(max_u)
    scc = SCC(vertexs, vertexs_r, max_u)
    scc.sort(reverse=True)
    print scc[0:5]

    #iarray = [1, 2, 3, 4, 5, 6, 7, 8]




if __name__ == "__main__":
    main()
