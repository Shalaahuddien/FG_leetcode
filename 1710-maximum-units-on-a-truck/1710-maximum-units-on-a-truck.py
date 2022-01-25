class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans, cap = 0, truckSize
        for b,u in boxTypes:
            if cap >= b:
                ans += b * u
                cap -= b
            else:
                ans += cap * u
                return ans
        return ans