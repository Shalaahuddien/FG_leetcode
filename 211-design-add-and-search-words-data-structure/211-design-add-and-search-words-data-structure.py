class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        p = self.root
        for c in word:
            p = p.setdefault(c, {})
        p['#'] = 1

    def search(self, word: str) -> bool:
        def q(s, p):
            for i, c in enumerate(s):
                if c not in p:
                    if c == '.':
                        for x in p:
                            if x != '#' and q(s[i + 1:], p[x]):
                                return True
                    return False
                else:
                    p = p[c]
            return '#' in p

        res = q(word, self.root)
        # print(word, res)
        return res
        
    # def _qry(self, s, p):
    #     for i,c in enumerate(s):
    #         if c != '.' and c not in p:
    #             return False
    #         if c == '.':
    #             ans = False
    #             return any(
    #                self._qry(ch + s[i+1:], p) for ch in p.keys()
    #             )
    #         p = p[c]
    #     return '#' in p


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)