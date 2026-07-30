# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node):
            if not node:
                return [0, True]
        
            left = traverse(node.left)
            right = traverse(node.right)
            
            print(left, right, node.val)

            heightCheck = abs(left[0] - right[0]) <= 1
            balanced = left[1] and right[1] and heightCheck

            return [max(left[0], right[0]) + 1, balanced]
        
        return traverse(root)[1]