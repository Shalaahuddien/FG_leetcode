class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cnt = Counter()                                         # <-- tracking counts of most-current letter in each uncompleted croak

        pre = {'r':'c', 'o':'r', 'a':'o', 'k':'a'}              # <-- map for preceding letters

        for ch in croakOfFrogs:
            if ch == 'c':                                       # <-- if ch == 'c', determine whether a frog who has croaked
                cnt['k'] -= 1 if cnt['k'] else 0                #     is ready to begin another croak; if so, decrement the  
                cnt['c'] += 1                                   #     value of cnt['k'] so we don't double-count the frog
                
            elif cnt[pre[ch]]:                                  # <-- if ch != 'c', and if pre[ch] != 0, update the current 
                cnt[pre[ch]] -= 1                               #     letter for a croak by decrement pre[ch]'s count and 
                cnt[ch] += 1                                    #     incrementing ch's count
            
            else: return -1                                     # <-- if ch has no the former letter (that is, cnt[pre[ch]]==0), 
                                                                #     then return -1

        return cnt['k'] if cnt.total() == cnt['k'] else -1      # <-- counts for all letters except for k should be zero; if
                                                                #     not, return -1. cnt[k] is the answer.