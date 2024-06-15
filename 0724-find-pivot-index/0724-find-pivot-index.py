# MY OWN
# FAIL, I wasn't sure how to sum while opearting for statement with left and right.
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
        
#         leftSum, rightSum = 0, 0
        
#         for i in range(len(nums)):
#             if nums.index(nums[i]) == 0:
#                 leftSum = 0
                
        
#         center = len(nums) // 2
#         leftMost, rightMost = 0, len(nums)
#         leftSum, rightSum = 0, 0
        
#         while leftMost <= center:
#             leftSum += nums[leftMost] 
        
#         while center < rightMost:
#             rightSum += nums[rightMost]
        
#         if leftSum == rightSum:
            
# Approach: Prefix Sum
# Time Comp: O(N)
# Space Comp: O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
        
            
            