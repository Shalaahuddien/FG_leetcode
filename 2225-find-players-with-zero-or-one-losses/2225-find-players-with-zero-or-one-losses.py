class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        DEG = Counter()
        for w, l in matches:
            DEG[l] += 1
            if w not in DEG:
                DEG[w] = 0
        ans = [[], []]
        for p, l in DEG.items():
            if l == 0:
                ans[0].append(p)
            if l == 1:
                ans[1].append(p)
        ans[0].sort()
        ans[1].sort()
        return ans