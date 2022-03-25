class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        R, M = Counter(ransomNote), Counter(magazine)
        for k, v in R.items():
            if k not in M or M[k] < v:
                return False
        return True
