class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        l = len(palindrome)
        ans = []
        if l == 1:
            return ''
        i = 0
        while i < l - 1:
            if palindrome[i] > 'a':
                break
            i += 1
        
        if i == l // 2 and l % 2 == 1:
            ans = palindrome[:-1] + 'b'
            return ''.join(ans)
        c = 'a'
        if palindrome[i] == 'a':
            c = 'b'
        ans = palindrome[:i] + c + palindrome[i + 1:]
        return ''.join(ans)