class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr)):
            p = arr[i : i + m]
            # BUG: if arr[i : i + m] * k in arr[i:]:
            if p * k == arr[i : i + m * k]:
                return True
        return False