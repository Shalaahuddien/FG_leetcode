class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needs, window = defaultdict(int), defaultdict(int)
        for c in t:
          needs[c] += 1
        l,r = 0,0 # [l,r)
        start, leng = 0, len(s)+1
        valid = 0
        
        while r < len(s):
          c = s[r]
          r += 1
          if c in needs:
            window[c] += 1
            if window[c] == needs[c]:
              valid += 1
          # print(l,r,window)
          # while (window needs shrink)
          while valid == len(needs):
            if leng >= r-l:
              start = l
              leng = r-l
            
            d = s[l]
            l += 1
            if d in needs:
              if needs[d] == window[d]:
                valid -= 1
              window[d] -= 1
        if leng == len(s)+1:
          return ''
        else:
          return s[start: start+leng]