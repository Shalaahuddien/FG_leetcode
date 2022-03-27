class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        enc = lambda s: [(k, len(list(grp))) for k, grp in groupby(s)]
        enc_name, enc_typed = enc(name), enc(typed)
        if len(enc_name) != len(enc_typed):
            return False
        for n, t in zip(enc_name, enc_typed):
            if n[0] != t[0]:
                return False
            if n[1] > t[1]:
                return False
        return True