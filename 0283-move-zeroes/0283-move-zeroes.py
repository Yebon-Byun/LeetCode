# MY OWN
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 nums.remove(nums[i])
#                 nums.append(0)
#             i += 1

# Discuss Section Approach
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        
        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

        