class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        lw = re.sub(r"[^a-zA-Z]", " ", paragraph).lower().split()
        Filter = Counter()
        for w in lw:
            if w not in set(banned):
                Filter[w] += 1
        return Filter.most_common(1)[0][0]