class Solution:
    def reverseVowels(self, s: str) -> str:
      vowels = set(list('aeiouAEIOU'))
      i, j = 0, len(s)-1

      res = list(s)
      while i < j:
          while i < j and s[i] not in vowels:
              i += 1
          while i < j and s[j] not in vowels:
              j -= 1
          res[i], res[j] = res[j], res[i]
          i, j = i+1, j-1
      return ''.join(res)