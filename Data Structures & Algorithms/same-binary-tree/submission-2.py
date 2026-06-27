# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while(stack):
            currPair = stack.pop()
            if currPair[0]==None and currPair[1]==None:
                continue
            else:
                if not currPair[1] or not currPair[0]:
                    return False
                if currPair[0].val != currPair[1].val:
                    return False
                stack.append((currPair[0].right,currPair[1].right))
                stack.append((currPair[0].left,currPair[1].left))
        return True
