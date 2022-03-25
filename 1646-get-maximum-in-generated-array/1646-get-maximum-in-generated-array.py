class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        mx = 1
        if n < 2:
            return n
        V = [0, 1]
        odd = False
        for i in range(2, n + 1):
            if odd:                    
                V.append(sum(V[i // 2 : i // 2 + 2]))
            else:
                V.append(V[i // 2])
            mx = max(mx, V[-1])
            odd = not odd
        return mx
