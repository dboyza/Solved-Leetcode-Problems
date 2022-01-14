
class MyHashSet:

    def __init__(self):
        self.bucket = []
        
    def add(self, key: int) -> None:
        index = hash(key)
        if key not in self.bucket:
            self.bucket.append(key)

    def remove(self, key: int) -> None:
        if key in self.bucket:
            self.bucket.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.bucket:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)