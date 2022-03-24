class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
            j = 0
            for w in words:
                if not s[j:].startswith(w):
                    return False
                j += len(w)
                if j == len(s):
                    return True
            return False