class Solution:
    def intToRoman(self, num: int) -> str:
        mp = {
            1000:'M',
            900:'CM',
            500:'D',
            400: 'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10:'X',
            9:'IX',
            5:'V',
            4:'IV',
            1: 'I'
        }
        rom = []
        for v,s in mp.items():
            if num == 0:
                break
            cnt, num = divmod(num, v)
            rom.append(cnt*s)
        return ''.join(rom)