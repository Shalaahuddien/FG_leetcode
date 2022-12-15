class Solution:

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def manhattan(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
                
        # init priority queue (cost, number of assigned workers, bikes status) 
        pq = [(0, 0, '0'*len(bikes))]
        
        # optimal cost amongst all paths to reach a node
        optimal = defaultdict(lambda:float('inf'))

        while pq:
            cost, i, bike_status = heapq.heappop(pq)
            
            # early stopping with termination condition 
            if i == len(workers):
                return cost            
            
            # generate successors. The next worker to be assigned is at index i
            for j, b in enumerate(bikes):
                if bike_status[j] != '1':
                    new_cost = cost + manhattan(workers[i], b)      
                    new_bike_status = bike_status[:j] + '1' + bike_status[j+1:]
                    
                    # update optimal cost if a new successor appears with lower cost to the same node
                    if new_cost < optimal[(i+1, new_bike_status)]:
                        optimal[(i+1, new_bike_status)] = new_cost
                        heapq.heappush(pq, (new_cost, i+1, new_bike_status))
                        
        return -1