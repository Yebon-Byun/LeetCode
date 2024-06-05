#MY OWN 
#FAIL

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#             if needle not in haystack:
#                 return -1
#             if needle in haystack:
#                 for i in range(len(haystack)):
#                     if needle[0] == haystack[i]:
#                         return i
#                     i += 1
                        
# Approach 1: Sliding Window
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)
        
        for window_start in range(n - m + 1):
            for i in range(m):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m - 1:
                    return window_start
        
        return -1
            
        
                
        