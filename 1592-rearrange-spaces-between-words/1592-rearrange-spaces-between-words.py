class Solution:
    def reorderSpaces(self, text: str) -> str:
        sp = text.count(' ')
        text = text.split()
        l = len(text)-1
        x,y = divmod(sp, l) if l else (0, sp)
        return (' '*x).join(text) + (' '*y)