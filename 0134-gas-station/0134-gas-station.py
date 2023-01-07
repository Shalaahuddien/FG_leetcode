class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, total_tank, cur_tank = 0, 0, 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            cur_tank += gas[i] - cost[i]
            if cur_tank < 0:
                start = i + 1
                cur_tank = 0
        return start if total_tank >= 0 else -1
        