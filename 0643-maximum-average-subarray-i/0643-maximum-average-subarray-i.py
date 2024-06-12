# MY OWN
# FAIL, I wans't sure how to move the subarray chunk at the same time.
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         total, comp = 0, 0
#         x = 0
        
#         while x < k - 1:
#             total += nums[x]
#             x += 1
        
# Approaching 1: Cumulative Sum
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])
        
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i-k]
            maxSum = max(maxSum, currSum)
            
        return maxSum / k