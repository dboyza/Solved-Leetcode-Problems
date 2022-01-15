
class MyHashSet:

    def __init__(self):
        self.bucket = [None] * 100000
    
    def hash(self, key):
        hash_key = key % 100000
        return hash_key

    def add(self, key: int) -> None:
        hash_key = self.hash(key)
        self.bucket[hash_key] = key

    def remove(self, key: int) -> None:
        
        hash_key = self.hash(key)
        if self.bucket[hash_key] != None:
            self.bucket[hash_key] = None

    def contains(self, key: int) -> bool:
        hash_key = self.hash(key)
        if self.bucket[hash_key] == None:
            return False
        return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)