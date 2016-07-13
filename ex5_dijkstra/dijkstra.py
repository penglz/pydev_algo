import heapq
from collections import defaultdict

def weight(pair): return pair[0]
def tail(pair): return pair[1]

def dijkstra(G, s):
    heap = []
    shortest_dist = {}
    shortest_dist[s] = 0
    dist_so_far = {}
#     init d
    for edge in G[s]:
        node = [edge[1],edge[0]]
        dist_so_far[edge[0]] = node
        heapq.heappush(heap, node)

    while len(shortest_dist) < len(G)-1:
        while True:
            w = heapq.heappop(heap)
            # grab the relevant parts of w
            node = tail(w)
            dist = weight(w)
            if node != -1:
                del dist_so_far[node]
                break
        shortest_dist[node] = dist
        
        for edge in G[node]:
            v = edge[0]
            if v not in shortest_dist:
                new_dist = dist + edge[1]
                new_entry = [new_dist, edge[0]]
                if v not in dist_so_far:
                    dist_so_far[v] = new_entry
                    heapq.heappush(heap, new_entry)
                elif new_dist < weight(dist_so_far[v]):
                    dist_so_far[v][1] = -1
                    dist_so_far[v] = new_entry
                    heapq.heappush(heap, new_entry)

    return shortest_dist

def main():

    G = defaultdict(list)


    with open('./dijkstraData.txt', 'r') as f:
        for line in f:
            vals = line.split()
            G[int(vals[0])] = map(lambda s: tuple(map(int,s.split(','))), vals[1:])


    result = dijkstra(G, 1)
    
    indexes = [7,37,59,82,99,115,133,165,188,197]
    print [result[x] for x in indexes]
          

    #iarray = [1, 2, 3, 4, 5, 6, 7, 8]




if __name__ == "__main__":
    main()
