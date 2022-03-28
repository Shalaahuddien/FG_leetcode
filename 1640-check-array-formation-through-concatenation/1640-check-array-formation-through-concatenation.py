class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        d = {p[0]: pi for pi, p in enumerate(pieces)}
        i = 0
        while i < n:
            # find target piece
            if arr[i] not in d:
                return False
            pi = d[arr[i]]
            target_piece = pieces[pi]
            for x in target_piece:
                if x != arr[i]:
                    return False
                i += 1
        return True