# In this programming problem and the next you'll code up the clustering algorithm 
# from lecture for computing a max-spacing k-clustering.
# 
# Input:
# clustering1.txt
# This file describes a distance function (equivalently, a complete graph with 
# edge costs). It has the following format:
# 
# [number_of_nodes]
# 
# [edge 1 node 1] [edge 1 node 2] [edge 1 cost]
# 
# [edge 2 node 1] [edge 2 node 2] [edge 2 cost]
# 
# 
# There is one edge (i,j) for each choice of 1<=i<j<=n where n is the number of nodes.
# 
# For example, the third line of the file is "1 3 5250", indicating that the 
# distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. 
# You can assume that distances are positive, but you should NOT assume that they are distinct.
# 
# Your task in this problem is to run the clustering algorithm from lecture on 
# this data set, where the target number k of clusters is set to 4. What is the maximum spacing of a 4-clustering?


from union_cut import UnionFind
import heapq

def dist(pair): return pair[0]
def head(pair): return pair[1]
def tail(pair): return pair[2]

def clustering(G, n):

    myunion = UnionFind(n)
    k = n
    
    while k > 4:
        while True:
            edge = heapq.heappop(G)
            # grab the relevant parts of w         
            u = tail(edge)
            v = head(edge)
            if not myunion.connected(u, v):
                break

        myunion.union(u, v)
        k -= 1   
    
    while len(G) > 0:
        edge = heapq.heappop(G)
        # grab the relevant parts of w         
        u = myunion.find_root(tail(edge))
        v = myunion.find_root(head(edge))
        d = dist(edge)
        if myunion.connected(u, v):
            continue
        
        return d

            
        
            
    
    
def main():

    G = []



    with open('./clustering1.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        for line in lines[1:]:
            u,v,c = map(int,line.split())
            heapq.heappush(G, [c, u-1, v-1])

    result = clustering(G, n)
    
    print result
          

    #iarray = [1, 2, 3, 4, 5, 6, 7, 8]




if __name__ == "__main__":
    main()