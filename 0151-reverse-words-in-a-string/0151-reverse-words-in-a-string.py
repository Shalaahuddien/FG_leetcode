class Solution:
    def reverseWords(self, s: str) -> str:
      def rev(a, l, r):
        # inclusive l & r
        while l < r:
          a[l],a[r] = a[r],a[l]
          l += 1
          r -= 1
      
      def rev_words(arr):
        l,r = 0,0
        while r < len(arr):
          while r < len(arr) and arr[r] != ' ': r += 1
          # now r right after word
          rev(arr, l,r-1)
          r += 1
          l = r
      
      s = ' '.join(s.split())
      arr = list(s)
      rev_words(arr)
      rev(arr, 0, len(arr)-1)
      return ''.join(arr)
      