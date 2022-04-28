class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        i = 0
        while i < len(citations) and citations[i] > i:
            i += 1
        # now we got i paper has citations greater or equal to i.
        return i