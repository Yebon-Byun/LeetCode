class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        ascending order : stricly increasing e.g.1 2 4 6 7
        non-decreasing order : increase, but never decrease e.g. 1 2 2 3 3 4 5 6 6
        
        nums1, nums2 : two integer arrays
        m, n : the number of elements in nums1 and nums2
        
        Order: Merge nums1 and nums2 into a single array soprted in non-decreasing order.
        result: 
        * not returend by the function
        * instead, stored inside the array nums1
        * nums1's length -> m + n
        * m elements denote the element that should be mergerd
        * n elements are set to 0 and should be ignored.
        * nums2's length -> n
        """
        
        # Approach 1 : Merge and sort
#         for i in range(n):
#             nums1[i+m] = nums2[i]
            
#         nums1.sort()
        
        # Time complexity : O((n+m)log(n+m))
        # Space complexity: O(n)
        # summary: nums1 뒤에 nums2 숫자들을 넣고 sort 한다.
        
        
        
        # Approach 2 : Three Pointers(Start From the Beginning)
        
#         nums1_copy = nums1[:m]
        
#         p1 = 0
#         p2 = 0
        
#         for p in range(n+m): #p = 0
#             if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]): 
#             #Q: How could I summarize this code?
#                 nums1[p] = nums1_copy[p1]
#                 p1 += 1
#             else:
#                 nums1[p] = nums2[p2] 
#                 p2 += 1
                
        # Time complexity : O(n+m)
        # Space complexity: O(m)
        
        
        # Approach 3 : Three Pointers(Start From the End)
        
        p1 = m - 1
        p2 = n - 1
        
        for p in range(n + m - 1, -1, -1):
            if p2 < 0 :
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
        
        
        
        
            
        
        