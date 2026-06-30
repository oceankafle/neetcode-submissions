class MyHashSet:

    def __init__(self):
        self.hashSet = []

    def add(self, key: int) -> None:
        self.hashSet.append(key)

    def remove(self, key: int) -> None:
        # find the key, delete it 
        nums = self.hashSet
        for i in range(len(nums)):
            if nums[i] == key:
                nums[i] = None

    def contains(self, key: int) -> bool:
        nums = self.hashSet
        for n in nums:
            if n == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)