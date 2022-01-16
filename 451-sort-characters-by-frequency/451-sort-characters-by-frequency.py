class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        ans = []
        for k,v in sorted(cnt.items(), key=lambda cf: (-cf[1], cf[0])):
            ans += [k]*v
        return ''.join(ans)