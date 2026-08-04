# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        msf = -101
        def dfs(node, msf):
            if not node:
                return 0
            
            if node.val >= msf:
                curr_score = 1
                msf = max(node.val, msf)
            else:
                curr_score = 0
            
            return curr_score + dfs(node.left, msf) + dfs(node.right, msf)
        
        return dfs(root, msf)

        
