# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_allowed, max_allowed):
            if not node:
                return True
            
            if node.val >= max_allowed or node.val <= min_allowed:
                return False
            
            lf = dfs(node.left, min_allowed, node.val)
            rt = dfs(node.right, node.val, max_allowed)
            
            return lf and rt
        
        return dfs(root, float('-inf'), float('inf'))