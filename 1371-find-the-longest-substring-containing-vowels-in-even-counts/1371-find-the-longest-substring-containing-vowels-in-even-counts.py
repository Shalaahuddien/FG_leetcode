class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        for l in range(len(s), -1, -1):
            # len(substr) = j-i+1 = l ===> j = l+i-1 < len(s) => i < len(s)-l+1
            for i in range(len(s) - l + 1):
                sub = s[i : i + l]
                for c in "aeiou":
                    if sub.count(c) % 2 != 0:
                        break
                else:
                    return l