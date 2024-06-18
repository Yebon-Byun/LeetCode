# MY OWN / Approach 1: Stack
# Time Comp: O(n)
# Space Comp: O(n)
class Solution:
    def removeStars(self, s: str) -> str:
        s_list = []
        for i in range(len(s)):
            if s[i] == "*":
                s_list.pop()
            else:
                s_list.append(s[i])
                
        return ''.join(s_list)
                
                