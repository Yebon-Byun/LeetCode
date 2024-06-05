# MY OWN
# string index out of range
# if s[i] != t[j]:

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i, j = 0, 0
#         comp_str = ""
#         while i < len(s):
#             while j < len(t):
#                 if s[i] == t[j]:
#                     comp_str += s[i]
#                     print(comp_str)
#                     i += 1
#                 if s[i] != t[j]:
#                     j += 1
#         return s == comp_str

# MY OWN(2)
# Time Comp: O(|T|)
# Spce Comp: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        comp_str = ""

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                comp_str += t[j]
                i += 1
            j += 1

        return comp_str == s
