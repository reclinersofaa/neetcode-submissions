# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str: #PreOrder logic
        self.treelist = []

        def helper(root):
            if not root:
                self.treelist.append("null")
                return

            self.treelist.append(str(root.val))

            helper(root.left)
            helper(root.right)

        helper(root)
        return ",".join(self.treelist)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "null":
            return None

        treelist = data.split(',')
        self.i = 0

        def helper():
            nodeval = treelist[self.i]
            self.i += 1 #So next recursive frame focuses on children
            
            if nodeval == "null":
                return 
            
            root = TreeNode(int(nodeval))

            root.left = helper()
            root.right  = helper()

            return root

        return helper()

