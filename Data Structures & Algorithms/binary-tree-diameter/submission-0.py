# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0

        def dfs(root):
            if root == None:
                return 0
            
            lf = dfs(root.left)
            rt = dfs(root.right)

            self.d = max(self.d, lf + rt)

            return 1 + max(lf, rt)

        dfs(root)

        return self.d