class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root, ans = {}, []
        def insert(s):
            p = root
            for c in s:
                p = p.setdefault(c, {})
            p['#'] = s
            
        def replace(s):
            p = root
            for c in s:
                p = p.get(c)
                if not p:
                    return s
                if '#' in p:
                    return p['#']
            return s
            
        for w in dictionary:
            insert(w)
            
        return ' '.join(map(replace, sentence.split()))
            