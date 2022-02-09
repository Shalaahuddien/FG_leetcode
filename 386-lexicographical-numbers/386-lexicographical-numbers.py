class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        v = 1
        while len(ans) < n:
            while v <= n:
                ans.append(v)
                v *= 10
            while v % 10 == 9 or v > n:
                v //= 10
            v += 1
        return ans