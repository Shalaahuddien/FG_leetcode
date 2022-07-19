class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        rm = defaultdict(int)
        lm = defaultdict(lambda: n-1)
        dist = defaultdict(lambda: -1)
        # forward
        for i in range(n):
            c = colors[i]
            for j in range(rm[c], i+1):
                dist[(j,c)] = i-j
            rm[c] = i+1
            
        # backward
        for i in range(n-1,-1,-1):
            c = colors[i]
            for j in range(lm[c], i, -1):
                dist[(j,c)] = min(j-i, dist[(j,c)] if dist[(j,c)] >= 0 else 2e9)
            lm[c] = i-1
        
        return (dist[(i,c)] for i,c in queries)
                