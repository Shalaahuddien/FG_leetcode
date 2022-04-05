class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre = 0
        ans = 0
        for n in gain:
            pre += n
            ans = max(ans, pre)
        return ans