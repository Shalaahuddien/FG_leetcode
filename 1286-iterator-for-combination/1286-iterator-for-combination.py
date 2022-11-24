class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.c = characters
        self.len = combinationLength
        self.state = ""
        
    def next(self):
        if self.state == "":
            self.state = self.c[:self.len]
        else:
            from os.path import commonprefix

            end = len(commonprefix([self.c[::-1], self.state[::-1]]))
            place = self.c.index(self.state[-end-1])
            self.state = self.state[:-end-1] + self.c[place + 1: place + 2 + end]
        return self.state

    def hasNext(self):
        return self.state != self.c[-self.len:]


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()