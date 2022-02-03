class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def nxt(C):
            out = [0]*8
            for i in range(1,7):
                if C[i-1] == C[i+1]:
                    out[i] = 1
            return out
        
        def rec(C,n):
            seen = {}
            for i in range(n):
                c = tuple(C)
                if c in seen:
                    cycle = i - seen[c]
                    return rec(C, (n-i)%cycle)
                else:
                    seen[c] = i
                    C = nxt(C)
            return C
        
        return rec(cells, n)