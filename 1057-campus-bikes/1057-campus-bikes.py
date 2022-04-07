class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
        for i, (x, y) in enumerate(workers):
            for j, (u, v) in enumerate(bikes):
                d = abs(x - u) + abs(y - v)
                distances.append((d, i, j))

        distances.sort()

        used_bikes = set()
        result = [-1] * len(workers)
        for dist, i, j in distances:
            if len(used_bikes) == len(workers):
                break
            # print(dist, i, j)
            if result[i] == -1 and j not in used_bikes:
                used_bikes.add(j)
                result[i] = j
        return result