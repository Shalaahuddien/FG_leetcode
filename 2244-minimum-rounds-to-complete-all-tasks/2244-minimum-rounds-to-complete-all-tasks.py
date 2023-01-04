class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        ans = 0
        for f in cnt.values():
            if f % 3 == 0:
                ans += f // 3
            elif f % 3 == 1:
                if f == 1:
                    return -1
                else:
                    ans += (f - 4) // 3 + 2
            else:  # == 2
                ans += f // 3 + 1
        return ans