# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Approach 1: Recursion
# Time Comp: O(n)
# Space Comp: O(logn)

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0
#         else:
#             left_h = self.maxDepth(root.left)
#             right_h = self.maxDepth(root.right)
        
#         return max(left_h, right_h) + 1

# Approach 2: Iteration
# Time Comp: O(n)
# Space Comp: O(logn)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            curr_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, curr_depth)
                stack.append((curr_depth + 1, root.left))
                stack.append((curr_depth + 1, root.right))
            
        return depth
            
        