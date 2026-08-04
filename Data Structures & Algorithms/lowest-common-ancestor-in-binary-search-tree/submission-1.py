# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
                #return self.lowestCommonAncestor(curr, p, q)
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
                #return self.lowestCommonAncestor(curr, p, q)
            else:
                return curr
        
        
        