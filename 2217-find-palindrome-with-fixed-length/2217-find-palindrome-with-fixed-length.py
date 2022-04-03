class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        l = intLength
        # 5 -> 2, 6 -> 2
        base = 10**((l-1)//2)
        res = [q-1+base for q in queries]
        for i,a in enumerate(res):
            # 5 -> 103->01. 6 -> 103->301
            b = str(a) + str(a)[-1-l%2::-1]
            res[i] = int(b) if len(b) == l else -1
        return res