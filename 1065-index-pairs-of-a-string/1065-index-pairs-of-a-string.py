class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        root, L, ans = {}, len(text), []
        
        def insert(s):
            p = root
            for c in s:
                p = p.setdefault(c, {})
            p['#'] = s
            
        for w in words:
            insert(w)
            
        for i in range(L):
            p = root
            for j in range(i,L):
                p = p.get(text[j])
                if not p:
                    break
                if '#' in p:
                    ans.append([i,j])
        return ans