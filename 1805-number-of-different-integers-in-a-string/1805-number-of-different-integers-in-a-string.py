class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = set()
        l, r = 0, 0
        while l < len(word):
            if word[l].isalpha():
                l += 1
            else:
                r = l
                while r < len(word) and word[r].isdigit():
                    r += 1
                nums.add(int(word[l:r]))
                l = r
        return len(nums)