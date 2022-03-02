class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        dif = None
        for x,y in zip(arr,arr[1:]):
            if dif is None:
                dif = y-x
            else:
                if dif != y-x:
                    return False
        return True