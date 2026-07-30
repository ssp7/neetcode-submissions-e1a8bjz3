# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def traverse(node):
            if not node:
                return 0
            
            lMax = traverse(node.left)
            rMax = traverse(node.right)
            nonlocal ans
            ans = max(ans, lMax + rMax)

            return max(lMax, rMax) + 1
        
        traverse(root)
        return ans