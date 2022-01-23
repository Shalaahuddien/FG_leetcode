class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = [[] for _ in range(2001)]
        for i, (x, y) in enumerate(workers):
            for j, (u, v) in enumerate(bikes):
                d = abs(x - u) + abs(y - v)
                distances[d].append((i, j))

        used_bikes = set()
        assign = [-1] * len(workers)
        for dist in distances:
            for w, b in dist:
                if assign[w] == -1 and b not in used_bikes:
                    used_bikes.add(b)
                    assign[w] = b
        return assign