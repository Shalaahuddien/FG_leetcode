class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        m, n = len(slots1), len(slots2)
        i = j = 0
        while i < m and j < n:
            intersectStart = max(slots1[i][0], slots2[j][0])
            intersectEnd = min(slots1[i][1], slots2[j][1])
            if intersectEnd - intersectStart >= duration:
                return [intersectStart, intersectStart + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []