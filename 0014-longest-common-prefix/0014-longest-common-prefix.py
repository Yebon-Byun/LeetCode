#MY OWN
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         """ 
#         Input: strs = ["flower","flow","flight"]
#         Output: "fl"
#         """
#         prefix = ""
#         for i in range(len(strs) - 1):
#             if strs[i][0] == strs[i+1][0]:
#                 prefix = strs[i][0]
#                 i += 1
#                 print(strs)
    
    
#Approach 1: Horizontal Scanning
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ""
#         prefix = strs[0]
#         for i in range(1, len(strs)):
#             while strs[i].find(prefix) != 0:
#                 prefix = prefix[0 : len(prefix) - 1]
#                 if prefix == "":
#                     return ""
#         return prefix

#Approach 2: Vertical scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]
                    
            