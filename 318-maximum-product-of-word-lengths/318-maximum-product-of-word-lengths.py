class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mx = 0
        ws = [set(w) for w in words]
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if ws[i].isdisjoint(ws[j]):
                    mx = max(mx, len(words[i]) * len(words[j]))
        return mx