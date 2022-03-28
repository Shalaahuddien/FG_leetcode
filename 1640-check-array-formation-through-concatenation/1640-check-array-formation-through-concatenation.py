class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces.sort(key=lambda x: x[0])
        p_len = len(pieces)
        n = len(arr)
        i = 0
        while i < n:
            left, right = 0, p_len - 1
            found = -1
            # use bisect to find target piece
            while left < right:
                mid = (left + right) // 2
                if pieces[mid][0] >= arr[i]:
                    right = mid
                else:
                    left = mid + 1
            target_piece = pieces[left]
            for x in target_piece:
                if x != arr[i]:
                    return False
                i += 1
        return True