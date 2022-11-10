class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for c in s:
            # if the current character is same as the last one in `ans`
            # then we cannot push it to `ans`
            # we remove the one in `ans`
            if ans and ans[-1] == c: ans.pop()
            # otherwise, add the current character to `ans`
            else: ans.append(c)
        return ''.join(ans)