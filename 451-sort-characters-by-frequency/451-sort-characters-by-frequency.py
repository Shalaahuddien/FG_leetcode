class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        sb = []
        for c, f in cnt.most_common():
            sb.append(c * f)
        return ''.join(sb)