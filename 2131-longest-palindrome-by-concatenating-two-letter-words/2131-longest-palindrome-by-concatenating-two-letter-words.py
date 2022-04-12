class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dif = defaultdict(lambda: [0, 0])
        sym = Counter()
        for w in words:
            if w != w[::-1]:
                signt = "".join(sorted(list(w)))
                if w == signt:
                    dif[signt][0] += 1
                else:
                    dif[signt][1] += 1
            else:
                sym[w] += 1
        cnt_d = cnt_s = 0
        for w in dif:
            cnt_d += min(dif[w])
        odd = False
        for w in sym:
            if sym[w] % 2:
                odd = True
            cnt_s += sym[w] // 2
        
        return (cnt_d + cnt_s) * 4 + odd * 2