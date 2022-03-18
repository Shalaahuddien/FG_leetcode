class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        ans = []
        for i, w in enumerate(words):
            for ow in words[i + 1 :]:
                if w in ow:
                    ans.append(w)
                    break
        return ans