class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start = set()
        for s in startWords:
            for c in ascii_lowercase:
                if c not in s:
                    start.add(''.join(sorted(s + c)))

        can = 0
        for t in targetWords:
            st = ''.join(sorted(t))
            if st in start:
                can += 1
        return can
