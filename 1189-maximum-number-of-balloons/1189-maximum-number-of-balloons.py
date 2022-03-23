class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        C = Counter(text)
        return min(C["b"], C["a"], C["l"] // 2, C["o"] // 2, C["n"])
