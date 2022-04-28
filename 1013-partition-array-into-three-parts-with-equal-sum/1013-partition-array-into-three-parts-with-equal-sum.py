class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        avg, remain, part, cnt = sum(arr) // 3, sum(arr) % 3, 0, 0
        for n in arr:
            part += n
            if part == avg:
                cnt += 1
                part = 0
        return remain == 0 and cnt >= 3