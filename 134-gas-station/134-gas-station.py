class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        total,cur = 0,0
        start = 0 
        for i in range(N):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                start = i+1
                cur = 0
        return start if total >= 0 else -1