class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        max_freq = max(cnt.values())

        # Bucket sort for the chars by freq
        buckets = defaultdict(list)
        for c, i in cnt.items():
            buckets[i].append(c)

        sb = []
        for b_size in range(max_freq, 0, -1):
            if b_size not in buckets:
                continue
            for c in buckets[b_size]:
                sb.append(c * b_size)
        return ''.join(sb)