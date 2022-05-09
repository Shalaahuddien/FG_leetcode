d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def bt(i, path, res):
            if i == len(digits):
                res.append(''.join(path))
                return
            for c in d[digits[i]]:
                bt(i+1, path+[c], res)
        res = []
        if not digits: return res
        bt(0, [], res)
        return res