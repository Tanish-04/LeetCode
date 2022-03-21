class MyHashSet:

    def __init__(self):
        self.array = []
        

    def add(self, key: int) -> None:
        self.array.append([key])

    def remove(self, key: int) -> None:
        try:
            while True:
                self.array.remove([key])
        except ValueError:
            pass
            
    def contains(self, key: int) -> bool:
        
        if [key] in self.array:
            return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)