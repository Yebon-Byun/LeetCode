class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        answer = [0] * len(nums)
        for i in range(len(nums)):
            total += nums[i]
            answer[i] = total
            i += 1
        return answer
            