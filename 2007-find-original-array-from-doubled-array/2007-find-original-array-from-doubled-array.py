class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        arr = sorted(changed)
        dq = deque([])
        res = []
        for i in arr:
            if dq and i == dq[0]:
                dq.popleft()
            else:
                dq.append(2*i)
                res.append(i)
        
        if dq:
            return []
        return res