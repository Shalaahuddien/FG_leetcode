class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def bt(sub_s, prev):
            if not sub_s:
                yield prev
            else:
                for i in range(1, len(sub_s) + 1):
                    ss = sub_s[:i]
                    if ss == ss[::-1]:
                        yield from bt(sub_s[i:], prev + [ss])
            
        return list(bt(s, []))