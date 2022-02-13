class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        vi = sorted([(v, i) for i, v in enumerate(arr)])
        ans = [None] * len(arr)
        pre = vi[0][0] - 1
        rank = 0
        for v, i in vi:
            if v == pre:
                ans[i] = rank
            else:
                rank += 1
                ans[i] = rank
                pre = v
        return ans
        