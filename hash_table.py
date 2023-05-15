class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                entry[1] = value
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self._hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                return entry[1]
        raise KeyError(key)
    
    def remove(self, key):
        index = self._hash(key)
        for i, entry in enumerate(self.table[index]):
            if entry[0] == key:
                del self.table[index][i]
                return
        raise KeyError(key)
