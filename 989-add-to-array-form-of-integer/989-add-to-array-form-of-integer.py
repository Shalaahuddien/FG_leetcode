class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)-1, -1, -1):
            k,num[i] = divmod(k + num[i], 10)
        if k:
            return [int(i) for i in str(k)] + num
        else:
            return num