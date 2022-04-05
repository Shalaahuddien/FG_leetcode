class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stk = []

        for i in range(n - 1, -1, -1):
            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()
            # now its mono-decr
            ans[i] = 0 if not stk else stk[-1] - i
            stk.append(i)
        return ans