# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Comp: O(n)
# Space Comp: O(n)
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, ans, level = float("-inf"), 0, 0 
        q = deque([root])
        
        
        while q:
            level += 1
            curr_level_sum = 0
            
            for _ in range(len(q)):
                node = q.popleft()
                curr_level_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if max_sum < curr_level_sum:
                max_sum, ans = curr_level_sum, level
            
        return ans
            
                
       
                
    