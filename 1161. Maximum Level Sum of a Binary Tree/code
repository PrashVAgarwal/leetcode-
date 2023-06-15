# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node,level):
            if not node:
                return
            
            if len(arr)==level:
                arr.append(node.val)
            else:
                arr[level]+=node.val
                
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            
        arr=[]
        dfs(root,0)
        
        return arr.index(max(arr)) +1
