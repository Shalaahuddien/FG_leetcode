class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        def win(l, r):
            return P[r + 1] - P[l]

        P = [0] * (len(arr) + 1)
        ans = 0
        for i in range(1, len(arr) + 1):
            P[i] = arr[i - 1] + P[i - 1]

        for sz in range(1, len(arr) + 1, 2):
            for l in range(len(arr)):
                if l + sz - 1 < len(arr):
                    ans += win(l, l + sz - 1)
        return ans
