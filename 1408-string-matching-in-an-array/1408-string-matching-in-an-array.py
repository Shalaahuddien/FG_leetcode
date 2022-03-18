class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        all_words = " ".join(words)
        ans = [w for w in words if all_words.count(w) >= 2]
        return ans
