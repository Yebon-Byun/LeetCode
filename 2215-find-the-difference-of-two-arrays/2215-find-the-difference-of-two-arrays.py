# MY OWN
# Time Comp: O(NM)
# Sapce Comp: O(N+M)

# class Solution:
#     def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
#         l1 = []
#         l2 = []
                
#         for i in range(len(nums1)):
#             if nums1[i] not in nums2:
#                 l1.append(nums1[i]) 
        
#         for j in range(len(nums2)):
#             if nums2[j] not in nums1:
#                 l2.append(nums2[j])
        
#         return [set(l1)] + [set(l2)]
    
# Approach: Use the set difference
# Time Comp: O(n + m)
# Space Comp: O(n + m)

# class Solution:
#     def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
#         set1 = set(nums1)
#         set2 = set(nums2)
        
#         return [list(set1.difference(set2)), list(set2.difference(set1))]
         
# Approach: python 1 liner
# Time Comp: O(n + m)
# Space Comp: O(n + m)
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]