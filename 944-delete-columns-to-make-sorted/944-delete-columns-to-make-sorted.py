class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        for col in zip(*strs):
            # print(col, sorted(col))
            if list(col) != sorted(col):
                cnt += 1
        return cnt