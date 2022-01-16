class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        seen = set(arr2)
        c, notin2 = Counter(arr1), []
        for n in arr1:
            if n not in seen:
                notin2.append(n)
        in2 = [] 
        for n in arr2:
            in2.extend(c[n] * [n])
                
        return in2 + sorted(notin2)