class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        A, i, j = list(s), 0, len(s) - 1
        while i < j:
            while i < j and not A[i].isalpha():
                i += 1
            while i < j and not A[j].isalpha():
                j -= 1
            A[i], A[j] = A[j], A[i]
            i, j = i + 1, j - 1
        return "".join(A)