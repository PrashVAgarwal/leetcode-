# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node,d):
            nonlocal ans
            if not node:
                ans=max(ans,d)
                return
            if not node.left:
                dfs(node.right,d+1)
            elif not node.right:
                dfs(node.left,d+1)
            else:
                dfs(node.left,d+1)
                dfs(node.right,d+1)
        
        dfs(root,0)
        return ans
