class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        idscore = defaultdict(list)
        for i,s in items:
            heappush(idscore[i], s)
            if len(idscore[i]) > 5:
                heappop(idscore[i])
        res = []
        for id in sorted(idscore.keys()):
            res.append(
                [id, sum(idscore[id])//5])
        return res