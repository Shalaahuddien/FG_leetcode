class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pick2 = lambda x: x * (x - 1) // 2
        cnt = Counter()
        for domi in dominoes:
            domi.sort()
            cnt[tuple(domi)] += 1
        return sum(map(pick2, cnt.values()))