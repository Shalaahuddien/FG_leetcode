class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt = defaultdict(int)
        for b in bills:
            if b == 5:
                cnt[5] += 1
            elif b == 10:
                if cnt[5] > 0:
                    cnt[5] -= 1
                    cnt[10] += 1
                else:
                    return False
            else:
                if cnt[5] > 0 and cnt[10] > 0:
                    cnt[5] -= 1
                    cnt[10] -= 1
                    cnt[20] += 1
                elif cnt[5] >= 3:
                    cnt[5] -= 3
                else:
                    return False
        return True