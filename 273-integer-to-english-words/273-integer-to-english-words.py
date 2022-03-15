class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        tens = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        bigs = {10**9: "Billion", 10**6: "Million", 1000: "Thousand"}
        def dfs(n):
            if n < 20:
                # return [to19[n-1]]
                return to19[n-1:n]
            elif n < 100:
                return [tens[n//10-2]] + dfs(n%10)
            elif n < 1000:
                return [to19[n//100-1]] + ['Hundred'] + dfs(n%100)
            else:
                for i in bigs:
                    if n // i > 0:
                        return dfs(n//i) + [bigs[i]] + dfs(n%i)
        return ' '.join(dfs(num)) or "Zero"