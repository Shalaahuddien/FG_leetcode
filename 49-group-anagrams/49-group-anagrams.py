class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            ss = tuple(sorted(s))
            d[ss].append(s)
        return d.values()