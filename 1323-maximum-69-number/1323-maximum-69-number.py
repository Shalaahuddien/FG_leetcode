class Solution:
    def maximum69Number (self, num: int) -> int:
        i = 0 
        tem = num
        sixidx = -1 
        while tem > 0:
            if tem % 10 == 6:
                sixidx = i  #refresh sixidx when found 6 at large digit.
            tem = tem//10
            i += 1
        return (num + 3 *(10**sixidx)) if sixidx != -1 else num