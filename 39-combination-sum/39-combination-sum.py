class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def bt(startIdx, remain, path, res):
            # print(startIdx, remain, path, res)
            if remain == 0:
                res.append(path[:])
                return
            for i in range(startIdx, len(candidates)):
                c = candidates[i]
                if c > remain:
                    # BUG: here i+1 then recurse, but the i in for loop will redo i+1!!! So duplicate!
                    bt(i + 1, remain, path, res)
                    # !XXX: if you call recursion multiple times, use RETURN!!!!!!!!!!
                    # !check labuladong sudoku backtracking
                    return
                else:
                    path.append(c)
                    bt(i, remain - c, path, res)
                    path.pop()

        candidates.sort(reverse=True)
        res = []
        bt(0, target, [], res)
        return res