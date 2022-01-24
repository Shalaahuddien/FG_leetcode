class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def insert(s):
            p = trie
            for c in root:
                p = p.setdefault(c, {})
            p['#'] = root

        def replace(s):
            p = trie
            for c in s:
                if c not in p:
                    return s
                p = p[c]
                if '#' in p:
                    return p['#']
            return s

        trie = {}
        for root in dictionary:
            insert(root)
        print(trie)
        return ' '.join(map(replace, sentence.split()))