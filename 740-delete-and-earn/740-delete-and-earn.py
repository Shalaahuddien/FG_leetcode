class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = Counter(nums)
        mx = max(nums)
        # print(points, mx)

        @cache
        def rob(v) -> int:
            if v > mx:
                return 0
            return max(points[v] * v + rob(v + 2), rob(v + 1))

        return rob(min(nums))