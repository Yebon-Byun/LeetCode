# MY OWN

import random

class RandomizedSet:

    def __init__(self):
        self.com = set()
        

    def insert(self, val: int) -> bool:
        if val in self.com:
            return False
        else:
            self.com.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.com:
            self.com.remove(val)
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        if self.com:
            return random.choice(tuple(self.com))
        else:
            return 0
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()