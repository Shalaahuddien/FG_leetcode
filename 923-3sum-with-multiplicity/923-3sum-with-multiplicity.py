class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        ans = 0
        for i in range(2, len(arr)):
            j,k = 0, i-1
            while j < k:
                sm = arr[i]+arr[j]+arr[k]
                if sm < target:
                    j +=1
                elif sm > target:
                    k -= 1
                else:
                    # count multiplicity of arr[j], arr[k]
                    l = r = 1
                    while j+l < k and arr[j] == arr[j+l]:
                        l += 1
                    while j+l <= k-r and arr[k] == arr[k-r]:
                        r += 1
                    ans += (l+r)*(l+r-1)//2 if arr[j] == arr[k] else l*r
                    j += l
                    k -= r
        return ans %(10**9+7)
            