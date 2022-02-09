class Solution:
    def reformatDate(self, date: str) -> str:
        dmy = date.split()
        d,m,y = 0,0,dmy[2]
        for c in dmy[0]:
            if c.isdigit():
                d = d*10 + int(c)
        mm = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        m = mm.index(dmy[1])+1
        return '-'.join([y,f'{m:02d}', f'{d:02d}'])