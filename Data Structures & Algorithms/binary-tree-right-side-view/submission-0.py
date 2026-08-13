# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq = collections.deque([root])
        ans = []
        
        while dq:
            level = []
            for _ in range(len(dq)):
                node = dq.popleft()
                if node:
                    dq.append(node.left)
                    dq.append(node.right)
                    level.append(node.val)
            if len(level):
                ans.append(level[-1])

        return ans