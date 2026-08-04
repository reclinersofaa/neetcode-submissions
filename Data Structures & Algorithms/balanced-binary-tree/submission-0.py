# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def Lengths(curr):
            if curr == None:
                return 0
            
            lf = Lengths(curr.left)
            rt = Lengths(curr.right)

            if lf == -1 or rt == -1:
                return -1

            bval = lf - rt
            if bval > 1 or bval < -1:
                return -1

            return 1 + max(lf, rt)
        
        res = Lengths(root)
        if res == -1:
            return False
        return True
        