class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dif = set()
        for e in emails:
            loc, dom = e.split("@")
            p = loc.find("+")
            if p == -1:
                p = len(loc)
            l = loc[:p].replace(".", "")
            dif.add(l + "@" + dom)
        return len(dif)
