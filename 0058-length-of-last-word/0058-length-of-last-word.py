#MY OWN
# Time Comp: O(N)
# Space Comp: O(N)
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         sep = s.split()
#         end = len(sep)
#         for i in reversed(range(len(sep))):
#             if len(sep[i]) >= 1:
#                 return len(sep[i])
            
#Approach 1: String Index Manipulation
# Time Comp: O(N)
# Space Comp: O(1)
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         p = len(s) - 1
#         while p >= 0 and s[p] == " ":
#             p -= 1
            
#         length = 0
#         while p >= 0 and s[p] != " ":
#             p -= 1
#             length += 1
            
#         return length

#Approach 2: One-loop Iteration
# Time Comp: O(N)
# Space Comp: O(1)
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         p, length = len(s), 0
        
#         while p > 0:
#             p -= 1
#             if s[p] != " ":
#                 length += 1
#             elif length > 0:
#                 return length
        
#         return length

#Approach 3: Built-in String Functions
# Time Comp: O(N) 
# Space Comp: O(N)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return 0 if not s or s.isspace() else len(s.split()[-1])
        
