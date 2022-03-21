class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = {c:i for i,c in enumerate(s)}
        anchor = l = 0
        parts = []
        for r,c in enumerate(s):
            anchor = max(anchor, last_pos[c])
            if r == anchor:
                parts.append(r-l+1)
                l = r+1
        return parts