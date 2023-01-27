class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        
        @cache
        def dp(s):
            for i in range(1, len(s)):
                if s[:i] not in wordset: continue
                if dp(s[i:]): return 2 # return 2 if can be break into more than 1 word in dictionary
            if s in wordset: return 1
            return 0
        
        return [w for w in words if dp(w) > 1]