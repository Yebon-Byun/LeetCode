#MY OWN - Fail
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = []
#         sum_up = 1
#         for i in range(len(nums)):
#             nums.remove(nums[i])
#             sum_up *= nums[i]
#             res.append(sum_up)
#         return res

# Approach 1 : Left and Right product lists
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        L, R, answer = [0]*length, [0]*length, [0]*length
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        for i in range(length):
            answer[i] = L[i] * R[i]
        
        return answer