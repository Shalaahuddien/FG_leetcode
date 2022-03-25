class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        def swap(A, i, j):
            A[i], A[j] = A[j], A[i]

        ss = list(s)
        for i in range(len(s)):
            while indices[i] != i:
                swap(ss, i, indices[i])
                swap(indices, i, indices[i])
                """
                ss[indices[i]], ss[i] = ss[i], ss[indices[i]]
                #! bug of Python
                indices[i], indices[indices[i]] = indices[indices[i]], indices[i]
                """
        return "".join(ss)