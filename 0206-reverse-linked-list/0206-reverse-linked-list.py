# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Approach 1: Iterative
#Time Comp: O(n)
#Space Comp: O(1)
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None
#         curr = head
#         while curr:
#             next_temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_temp
            
#         return prev
    
#Approahc 2: Recursive
#Time Comp: O(n)
#Space Comp: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
