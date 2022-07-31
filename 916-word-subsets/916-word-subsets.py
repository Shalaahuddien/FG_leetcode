class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cnt = Counter()
        for b in B:
            cnt |= Counter(b)
            
        return [a for a in A if not cnt - Counter(a)]