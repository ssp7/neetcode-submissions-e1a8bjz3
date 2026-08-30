# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []
        def preorder(node):
            if not node:
                return
            
            preorder(node.left)
            nodes.append(node.val)
            preorder(node.right)
        
        preorder(root)

        for idx in range(len(nodes) - 1):
            if nodes[idx] >= nodes[idx + 1]:
                return False
        return True