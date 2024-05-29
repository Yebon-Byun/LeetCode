class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sep = s.split()
        end = len(sep)
        for i in reversed(range(len(sep))):
            if len(sep[i]) >= 1:
                return len(sep[i])
            
        