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
        res = set()
        for w in words:
            morse = "".join([MORSE[ord(c) - ord("a")] for c in w])

            res.add(morse)
        return len(res)
