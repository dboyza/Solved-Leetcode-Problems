class MyHashMap:

    def __init__(self):
        self.bucket = [None] * 100000

    def hash(self, key):
        hash_key = key % 100000
        return hash_key
    
    def put(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        self.bucket[hash_key] = value

    def get(self, key: int) -> int:
        hash_key = self.hash(key)
        if self.bucket[hash_key] == None:
            return -1
        return self.bucket[hash_key]

    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        if self.bucket[hash_key] != None:
            self.bucket[hash_key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)