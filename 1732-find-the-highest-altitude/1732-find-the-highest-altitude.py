# MY OWN
# Time Comp: O(N)
# Space Comp: O(1)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total = max_alt = 0
        
        for i in range(len(gain)):
            total += gain[i]
            max_alt = max(total, max_alt)
        
        return max_alt
            