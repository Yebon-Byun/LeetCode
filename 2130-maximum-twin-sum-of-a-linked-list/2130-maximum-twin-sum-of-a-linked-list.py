# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# MY OWN
# I wasn't sure how to access the value in a located certain value having an index. I think an idea to get the value through the index is a wrong approach.
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         if head.next == None: return None
        
#         curr = head
#         length = 0
#         max_num = 0
        
#         while curr:
#             length += 1
#             curr = curr.next
            
#         curr = head
#         for i in range(length):
#             twin_index = length - 1 - i
#             value1 = curr.val
#             print(value1)


# Approach 1: Usinig List of Integers
# Time Comp: O(n)
# Space Comp: O(n)

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        values = []
        
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        i = 0
        j = len(values) - 1
        maxSum = 0
        while (i < j):      
            maxSum = max(maxSum, values[i] + values[j])
            i = i + 1
            j = j - 1
            
        return maxSum
        
        
        
        
        
        
        