class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
        
#         nums : an integer arrahy
#         Q: rotate the array to the right by k steps, where k is non-negative.
#         R: do not return anything, modifyt nums in-place instead.
        
        
        
#         Approach 0 : by myself

#         Approach 1 : Brute Force
        
#         The simplest approach is to rotate all the elemenets of the arry in k steps
#         by rotating the elements by 1 unit in each step.
        
        
        
#         Approach 2 : Using Extra Array
        
#         we will use an extra arry in which we place every element of the array at its 
#         correct position.
#         i.e. the number at index i in the original array is placed at the index
#         (i+k) % length of array => we could put the element into 'k'th
#         order if we follow this, while looping with for statement.
#         Then, we copy the new array to the oirignal one.
        
        
#         Approach 3 : Using Cyclic Repalcements
        
#         we can directly place every number of the array at its required correct position.
#         But if we do that, we wil destoy the original element the number being replaced 
#         in a temp variable. Then, we can place the replaced number(temp) at its correct
#         position and so on,
        
        
        
#         Approach 4 : Using Reverse
        
#         This approach is based on the fact that when we rotate the array k times, k
#         elements from the back end of the array come to the front and the rest of the
#         elements from the front shift backwards.
        
#         In this approach, we firstly reverse all the elements of the array. Then, 
#         reversing the first k elements followed by reversing the rest n - k elements
#         gives us the required result.
        
#         """
        


        #0
        # class Solution:
        #         def rotate(self, nums: List[int], k: int) -> None:
        #                 """
        #                 Do not return anything, modify nums in-place instead.
        #                 """
        #                 while k:
        #                 num = nums.pop()
        #                 nums.insert(0, num) 
        #                 k -= 1
        #                 if k == 0:
        #                         break
                        
        #                 return nums
        


        #1
#         k %= len(nums)
        
#         for i in range(k):
#             previous = nums[-1]
#             for j in range(len(nums)): 
#                 nums[j], previous = previous, nums[j]
    
        #2
#         n = len(nums)
#         a = [0] * n
#         for i in range(n):
#             a[(i + k) % n] = nums[i]
            
#         nums[:] = a

        #3
        # unsolved
        
        #4 
        
# class Solution:
#     def reverse(self, nums: list, start: int, end: int) -> None:
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start, end = start + 1, end - 1
            
#     def rotate(self, nums: List[int], k: int) -> None:
        
#         n = len(nums)
#         k %= n
        
#         self.reverse(nums, 0, n - 1)
#         self.reverse(nums, 0, k - 1)
#         self.reverse(nums, k, n - 1)
            
        #5 from the discussion section
        # k %= len(nums)
        # nums[:] = nums[-k:] + nums[:-k]
        
        
        
        
        
        