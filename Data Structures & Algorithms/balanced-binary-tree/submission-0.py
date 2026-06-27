# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self,root:Optional[TreeNode]):
        if not root:
            return 0
        leftD = self.maxDepth(root.left)
        rightD = self.maxDepth(root.right)
        if abs(leftD-rightD) > 1:
            self.bal = False
        return 1 + max(leftD,rightD)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True
        self.maxDepth(root)
        return self.bal