# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# MY OWN
# FAIL
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         good_list = []
#         left_comp, right_comp = 0, 0
#         if root is not None:
#             good_list.append(root.val)
#         else:
#             left_good = self.goodNodes(root.left)
#             good_list.append(left_comp)
#             right_good = self.goodNodes(root.right.val)
#             right_good = max(right_comp, right_good)
#             good_list.append(right_comp)
#         return good_list

# Approach 1: DFS, Recursion
# Time Comp: O(n)
# Space Comp: O(n)
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         def dfs(node, max_so_far):
#             nonlocal num_good_nodes
#             if max_so_far <= node.val:
#                 num_good_nodes += 1
#             if node.right:
#                 dfs(node.right, max(node.val, max_so_far))
#             if node.left:
#                 dfs(node.left, max(node.val, max_so_far))    
#         num_good_nodes = 0
#         dfs(root, float("-inf"))
#         return num_good_nodes

# Approach 2: DFS, Iterative
# Time Comp: O(n)
# Space Comp: O(n)
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         stack = [(root, float("-inf"))]
#         num_good_nodes = 0
#         while stack:
#             node, max_so_far = stack.pop()
#             print("node", node)
#             print("max_so_far", max_so_far)
#             if max_so_far <= node.val:
#                 num_good_nodes += 1 
#             if node.left:
#                 stack.append((node.left, max(node.val, max_so_far)))
#             if node.right:
#                 stack.append((node.right, max(node.val, max_so_far)))
#         return num_good_nodes

# Approach 3: BFS
# Time Comp: O(n)
# Space Comp: O(n)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good_nodes = 0
        
        # Use collections.deque for efficient popping
        queue = deque([(root, float("-inf"))])
        while queue:
            node, max_so_far = queue.popleft()
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.right:
                queue.append((node.right, max(node.val, max_so_far)))
            if node.left:
                queue.append((node.left, max(node.val, max_so_far)))
        
        return num_good_nodes
        

        
