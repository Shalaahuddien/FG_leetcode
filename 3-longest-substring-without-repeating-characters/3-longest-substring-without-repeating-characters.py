class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        wind = defaultdict(int)
        l,r = 0,0
        longest = 0
        while r < len(s):
          c = s[r]
          r += 1
          wind[c] += 1
          
          while wind[c] != 1:
            d = s[l]
            l += 1
            # if d == c:
            wind[d] -= 1
          # now wind is valid wihtout repeat chars
          # time to staging, note: window: [l,r), so leng = r-l
          longest = max(longest, r-l) 
        return longest