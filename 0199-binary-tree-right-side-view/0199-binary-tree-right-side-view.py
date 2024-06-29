# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# MY OWN
# 
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         def bfs(node):
#             if node is None: return []
#             if node.right:
#                 return bfs(node.right)

from typing import Optional, List

# TreeNode 클래스가 이미 정의되어 있다고 가정합니다.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        rightside = []

        def bfs(node, level):
            if node is None:
                return
            
            if level == len(rightside):
                rightside.append(node.val)

            bfs(node.right, level + 1)
            bfs(node.left, level + 1)

        bfs(root, 0)
        return rightside


# class Solution:
#     def rightSideView(self, root: TreeNode) -> List[int]:
#         if root is None:
#             return []

#         next_level = deque(
#             [
#                 root,
#             ]
#         )
#         rightside = []

#         while next_level:
#             # prepare for the next level
#             curr_level = next_level
#             next_level = deque()

#             while curr_level:
#                 node = curr_level.popleft()

#                 # add child nodes of the current level
#                 # in the queue for the next level
#                 if node.left:
#                     next_level.append(node.left)
#                 if node.right:
#                     next_level.append(node.right)

#             # The current level is finished.
#             # Its last element is the rightmost one.
#             rightside.append(node.val)

#         return rightside