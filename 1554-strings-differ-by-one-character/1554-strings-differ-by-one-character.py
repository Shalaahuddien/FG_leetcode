class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        n, m = len(dict), len(dict[0])
        hashes = [0] * n
        MOD = maxsize

        for i in range(n):
            for j in range(m):
                hashes[i] = (26 * hashes[i] + (ord(dict[i][j]) - ord("a"))) % MOD

        base = 1
        for j in range(m - 1, -1, -1):
            seen = set()
            for i in range(n):
                new_h = (hashes[i] - base * (ord(dict[i][j]) - ord("a"))) % MOD
                if new_h in seen:
                    return True
                seen.add(new_h)
            base = 26 * base % MOD
        return False