class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [
                ".-",
                "-...",
                "-.-.",
                "-..",
                ".",
                "..-.",
                "--.",
                "....",
                "..",
                ".---",
                "-.-",
                ".-..",
                "--",
                "-.",
                "---",
                ".--.",
                "--.-",
                ".-.",
                "...",
                "-",
                "..-",
                "...-",
                ".--",
                "-..-",
                "-.--",
                "--..",
            ]
        c2m = {c: m for c, m in zip(ascii_lowercase, MORSE)}
        res = set()
        for w in words:
            morse = "".join([c2m[c] for c in w])
            res.add(morse)
        return len(res)
