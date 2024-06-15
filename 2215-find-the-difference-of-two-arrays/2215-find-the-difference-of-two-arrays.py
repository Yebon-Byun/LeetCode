class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1 = []
        l2 = []
                
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                l1.append(nums1[i]) 
        
        for j in range(len(nums2)):
            if nums2[j] not in nums1:
                l2.append(nums2[j])
        
        return [set(l1)] + [set(l2)]
                