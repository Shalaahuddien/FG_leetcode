class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        w2b_list = []
        used_bikes = set()
        ans = [-1] * len(workers)
        pq = []
        for i, (x,y) in enumerate(workers):
            cur_wb_pairs = []
            for j, (u,v) in enumerate(bikes):
                d = abs(x-u) + abs(y-v)
                cur_wb_pairs.append((d, i,j))
            cur_wb_pairs.sort(reverse=True)
            heappush(pq, cur_wb_pairs.pop())
            w2b_list.append(cur_wb_pairs)
            
        while pq:
            if len(used_bikes) == len(bikes):
                break
            d,w,b = heappop(pq)
            if ans[w] == -1 and b not in used_bikes:
                used_bikes.add(b)
                ans[w] = b
            else:
                next_closet_bike = w2b_list[w].pop()
                heappush(pq, next_closet_bike)
                
        return ans
            