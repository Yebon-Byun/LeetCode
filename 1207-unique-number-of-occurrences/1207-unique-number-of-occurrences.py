# MY OWN
# FAIL, I wasn't sure how to compare values in dictionary.
# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         comp = 0
#         u_arr = set(arr)
 
#         v_arr = []
#         comp1, comp2 = 0, 0
#         dict = {i : 0 for i in arr}
#         for i in arr:
#             dict[i] += 1
        
#         first_value = next(iter(dict.values()))
#         all_same = all(value == first_value for value in dict.values())
        
        
#         if all_same:
#             return False
#         else:
#             return True

# Approahc 1: Counter
# Time Comp: O(n)
# Space Comp: O(n)
# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         return len(set(Counter(arr).values())) == len(set(arr))

# Approach 2: Counter & Set
# Time Comp: O(n)
# Space Comp: O(n)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        s = set()
        for i in c.values():
            if i not in s:
                s.add(i)
            else:
                return False
        return True
            
            