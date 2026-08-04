# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.pathsum = float('-inf')

        def dfs(root):
            if not root:
                return 0
            
            lf = max(0, dfs(root.left))
            rt = max(0, dfs(root.right))

            self.pathsum = max(self.pathsum, lf + rt + root.val)

            return root.val + max(lf, rt)
        
        dfs(root)

        return self.pathsum

