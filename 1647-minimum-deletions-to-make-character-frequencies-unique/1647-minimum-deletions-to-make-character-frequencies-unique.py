class Solution:
    def minDeletions(self, s: str) -> int:
        s = "".join(sorted(s))
        cnt = Counter(s)
        freq = sorted(cnt.values(), reverse=True)
        ans = 0
        for i in range(1, len(freq)):
            if freq[i] >= freq[i - 1]:
                to = freq[i - 1] - 1
                if to < 0:
                    to = 0
                ans += freq[i] - to
                freq[i] = to
        print("new: ", freq)
        return ans