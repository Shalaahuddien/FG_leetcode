class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dep = 0
        for l in logs:
            if l.startswith("../"):
                dep -= 1
                dep = max(dep, 0)
            elif l.startswith("./"):
                continue
            else:
                dep += 1
        return max(0,dep)
