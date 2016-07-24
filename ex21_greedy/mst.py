import heapq
from collections import defaultdict

def weight(pair): return pair[0]
def tail(pair): return pair[1]

def mst(G):
    s = 1
    heap = []
    m_s_t = [s]
    cost = 0
    dist_so_far = {}
#     init d
    for edge in G[s]:
        dist_so_far[tail(edge)] = edge
        heapq.heappush(heap, edge)

    while len(m_s_t) < len(G):
        while True:
            w = heapq.heappop(heap)
            # grab the relevant parts of w
            node = tail(w)
            dist = weight(w)
            if node != -1:
                del dist_so_far[node]
                break
        cost = cost + dist
        m_s_t.append(node)
        
        for edge in G[node]:
            v = tail(edge)
            if v not in m_s_t:
                new_dist = weight(edge)
                new_entry = edge
                if v not in dist_so_far:
                    dist_so_far[v] = new_entry
                    heapq.heappush(heap, new_entry)
                elif new_dist < weight(dist_so_far[v]):
                    dist_so_far[v][1] = -1
                    dist_so_far[v] = new_entry
                    heapq.heappush(heap, new_entry)

    return cost

def main():

    G = defaultdict(list)


    with open('./edges.txt', 'r') as f:
        for line in f.readlines()[1:]:
            u,v,c = map(int,line.split())
            G[u].append([c,v])
            G[v].append([c,u])


    result = mst(G)
    
    print result
          

    #iarray = [1, 2, 3, 4, 5, 6, 7, 8]




if __name__ == "__main__":
    main()