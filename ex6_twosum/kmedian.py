import heapq

def main():
    heap_low = []
    heap_high = []
    mysum = 0
    with open('./Median.txt', 'r') as f:
        lines = f.readlines()
        val0 = int(lines[0])
        val1 = int(lines[1])
        mysum += val0
        if val0 <= val1:
            heapq.heappush(heap_low, -val0)
            heapq.heappush(heap_high, val1)
            mysum += val0
        else:
            heapq.heappush(heap_low, -val1)
            heapq.heappush(heap_high, val0)
            mysum += val1
            
        for line in lines[2:]:
            val = int(line)
            val_high = heap_high[0]
            
            if val < val_high:
                heapq.heappush(heap_low, -val)
            else:
                heapq.heappush(heap_high, val)
            
            if len(heap_low) - len(heap_high) > 1:
                movval = -heapq.heappop(heap_low)
                heapq.heappush(heap_high, movval)
            elif len(heap_high) - len(heap_low) > 0:
                movval = heapq.heappop(heap_high)
                heapq.heappush(heap_low, -movval)
                
            mysum += -(heap_low[0])
                
    

                 
    print mysum
    print mysum % 10000

    #iarray = [1, 2, 3, 4, 5, 6, 7, 8]




if __name__ == "__main__":
    main()