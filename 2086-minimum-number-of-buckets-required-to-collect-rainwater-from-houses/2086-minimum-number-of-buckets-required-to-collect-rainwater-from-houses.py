class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street)
        i, ans = 0, 0
        while i < n:
            if street[i] == "H":
                if i + 1 < n and street[i + 1] == ".":
                    ans += 1
                    i += 2
                elif i - 1 >= 0 and street[i - 1] == ".":
                    ans += 1
                else:
                    return -1
            i += 1
        return ans