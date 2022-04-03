class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.d = {k: v for k, v in zip(keys, values)}
        # (2) The second hashmap self.dictmap is a Counter - we encrypt each word in the given dictionary and use the
        # encrypted string as the key and increase the counter by 1. As such, we have solved the duplication problem
        # of the decrypt() method.
        self.freq = Counter()
        for word in dictionary:
            self.freq[self.encrypt(word)] += 1

    def encrypt(self, word1: str) -> str:
        return "".join([self.d[c] for c in word1])

    def decrypt(self, word2: str) -> int:
        return self.freq[word2]


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)