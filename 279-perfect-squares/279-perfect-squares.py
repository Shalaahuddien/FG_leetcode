class Solution:
    def numSquares(self, n: int) -> int:
        evens = [i**2 for i in range(1, int(n**0.5) + 1)]

        d, q = 1, deque([n])
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                for e in evens:
                    if x == e:
                        return d
                    if x < e:
                        break
                    q.append(x - e)
            d += 1
        return d