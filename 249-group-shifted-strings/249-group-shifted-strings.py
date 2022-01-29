class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_hash(s):
            key = []
            for x,y in zip(s, s[1:]):
                key.append(chr((ord(y) - ord(x)) % 26 + ord('a')))
            return ''.join(key)
        
        groups = defaultdict(list)
        for s in strings:
            key = get_hash(s)
            groups[key].append(s)
        return list(groups.values())