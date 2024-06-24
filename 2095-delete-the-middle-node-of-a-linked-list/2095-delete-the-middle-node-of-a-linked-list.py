# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# MY OWN
# Time Comp: O(n)
# Space Comp: O(1)

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return None
        
        curr = head
        length = 0
        
        while curr:
            length += 1
            curr = curr.next
        
        middle_node = length // 2
        
        curr = head
        for _ in range(middle_node - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        
        return head
            