class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            pre = list(arr)
            for i in range(1, len(arr) - 1):
                if pre[i] < min(pre[i - 1], pre[i + 1]):
                    arr[i] += 1
                elif pre[i] > max(pre[i - 1], pre[i + 1]):
                    arr[i] -= 1
            if pre == arr:
                return arr