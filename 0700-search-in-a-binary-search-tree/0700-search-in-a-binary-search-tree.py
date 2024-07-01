# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# MY OWN
# FAIL, I didn't remember how to manipulate BST.
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if root is None: return []
        # q = deque([root])
        # def bst(node):
        #     print(node)
        #     if node is None: return []
        #     if node.left:
        #         bst(node.left)
        #         s = q.popleft()
        #     if node.right:
        #         bst(node.right)
        #         s = q.popleft()
        #     if s == val:
        #         return s
        # bst(root)
        # return 

# Approach 1: Recursion
# Time Comp: O(H)
# Space Comp: O(H)
# class Solution:
#     def searchBST(self, root: TreeNode, val: int) -> TreeNode:
#         if root is None or val == root.val:
#             return root
#         return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)
    

# Approach 2: Iteration
# Time Comp: O(H)
# Space Comp: T(N)
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root
                
            
            
            
        