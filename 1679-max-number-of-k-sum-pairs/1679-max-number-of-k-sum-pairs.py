#MY OWN
#FAIL
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         total_op = 0
#         for i in range(len(nums)):
#             if k - nums[i] in nums:
#                 total_op += 1
#         return total_op
    
#Approach 1: Two Pointer
#Time Comp: O(n log n)
#Space Comp: O(1)
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         print(nums)
        
#         left = 0
#         right = len(nums) - 1
#         operation = 0
        
#         while left < right:
#             if ((nums[left] + nums[right]) == k):
#                 operation += 1
#                 left += 1
#                 right -= 1
#             elif ((nums[left] + nums[right]) < k):
#                 left += 1
#             else:
#                 right -= 1
#         return operation

# Approach 2: Defaultdict
# Time Comp: O(n)
# Space Comp: O(n)
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        comps = defaultdict(int)
        ops = 0
        
        for n in nums:
            # print("n:", n)
            # print("comps:", comps)
            if comps[n] > 0:
                ops += 1
                comps[n] -= 1
            else:
                comp = k - n
                comps[comp] += 1
        return ops

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
