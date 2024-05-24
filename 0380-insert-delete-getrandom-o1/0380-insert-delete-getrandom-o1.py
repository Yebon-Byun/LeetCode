# MY OWN

# import random
# class RandomizedSet:

#     def __init__(self):
#         self.com = set()
        

#     def insert(self, val: int) -> bool:
#         if val in self.com:
#             return False
#         else:
#             self.com.add(val)
#             return True

#     def remove(self, val: int) -> bool:
#         if val in self.com:
#             self.com.remove(val)
#             return True
#         else:
#             return False
        
#     def getRandom(self) -> int:
#         if self.com:
#             return random.choice(tuple(self.com))
#         else:
#             return 0
        
    
# Approach 1 : HashMap + ArrayList
# the reason

from random import choice
class RandomizedSet:

    def __init__(self):
        "Initialize your data structrue here."
        self.dict = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            self.list.pop()
            del self.dict[val]
            return True
        return False
        
    def getRandom(self) -> int:
        return choice(self.list)
        

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()