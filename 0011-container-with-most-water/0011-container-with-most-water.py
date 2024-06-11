#MY OWN
#FAIL, I wanted to get every elemenets in list record where they are.
#But, there's no way to utilize tuples.
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         t = {}
#         for height, i in enumerate(height, start=1):
#             t[0] = (height, i)
            
#Approach 1: Bruth Force / 완전탐색
#Time Comp: O(n^2)
#Space Comp: O(1)
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         maxarea = 0
#         for left in range(len(height)):
#             for right in range(left + 1, len(height)):
#                 width = right - left
#                 maxarea = max(maxarea, min(height[left], height[right]) * width)
#         return maxarea

#Approach 2: Two Pointer Approach
#Time Comp: O(n)
#Space Comp: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1 
        
        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            
        return maxarea



            