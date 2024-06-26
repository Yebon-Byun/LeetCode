# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# MY OWN
# Occured Time Limit Exceeded
# class Solution:
#     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#         def rootOne(root1):
#             root1_list = []
#             while root1:
#                 if root1.left:
#                     rootOne(root1.left)
#                     if root1.left == None and root1.right == None:
#                         root1_list.append(root1.val)
#                 if root1.right:
#                     rootOne(root1.right)
#                     if root1.right  == None and root1.right == None:
#                         root1_list.append(root1.val)
#             return root1_list
                        
#         def rootTwo(root2):
#             root2_list = []
#             while root2:
#                 if root2.left:
#                     rootTwo(root2.left)
#                     if root2.left == None and root2.right == None:
#                         root2_list.append(root2.val)
#                 if root2.right:
#                     rootTwo(root2.right)
#                     if root2.right  == None and root2.right == None:
#                         root2_list.append(root2.val)
#             return root2_list
        
#         return rootOne(root1) == rootTwo(root2)
#         rootOne(root1)
#         rootTwo(root2)
#         root1_list = []
#         print(root1_list)
#         root2_list = []
#         print(root2_list)
        
#         if root1_list == root2_list:
#             return True
#         else:
#             return False

# Approach 1: DFS, yield & yield from
# Time Comp: O(n)
# Space Comp: O(n)
# class Solution:
    # def leafSimilar(self, root1, root2):
    #     def dfs(node):
    #         if node:
    #             if not node.left and not node.right:
    #                 yield node.val
    #             yield from dfs(node.left)
    #             yield from dfs(node.right)
    #     return list(dfs(root1)) == list(dfs(root2))
        
# Approach 2: DFS, old shcool
# Time Comp: O(n)
# Space Comp: O(n)
class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return dfs(node.left) + dfs(node.right)

        root1_leaves = dfs(root1)
        root2_leaves = dfs(root2)
        
        return root1_leaves == root2_leaves



                    