class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def bt(start, path, res):
            if sum(path)>target:
                return
            elif sum(path) == target:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                bt(i, path+[candidates[i]], res)
        res = []
        bt(0, [], res)
        return res