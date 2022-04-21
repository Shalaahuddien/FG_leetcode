class MyHashSet:

    def __init__(self):
        self.base = 799
        self.hash_set = [[] for i in range(self.base)]
    
    def hash_key(self, key: int):
        return key%self.base
    
    def add(self, key: int) -> None:
        hash_pos = self.hash_key(key)
        if key in self.hash_set[hash_pos]:
            pass
        else:
            self.hash_set[hash_pos].append(key)

    def remove(self, key: int) -> None:
        hash_pos = self.hash_key(key)
        if key not in self.hash_set[hash_pos]:
            pass
        else:
            self.hash_set[hash_pos].remove(key)

    def contains(self, key: int) -> bool:
        hash_pos = self.hash_key(key)
        if key in self.hash_set[hash_pos]:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)