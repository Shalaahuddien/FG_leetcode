class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p2s, s2p = defaultdict(str), defaultdict(str)
        if len(pattern) != len(s.split()):
            return False
        for a, b in zip(pattern, s.split()):
            c = p2s[a]
            d = s2p[b]
            if c == d == '':
                p2s[a] = b
                s2p[b] = a
            elif c != b or d != a:
                return False
        return True