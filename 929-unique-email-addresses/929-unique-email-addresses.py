class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dif = set()
        for e in emails:
            loc, dom = e.split("@")
            l = loc.split("+")[0].replace(".", "")
            dif.add(l + "@" + dom)
        return len(dif)
