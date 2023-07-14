# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append((root,1))
        #ans=float("inf")
        if not root:
            return 0
        while q:
            l=len(q)
            for i in range(l):
                node,depth=q.popleft()
                if node.left==None and node.right==None:
                    return depth
                elif node.left==None:
                    q.append((node.right,depth+1))
                elif node.right==None:
                    q.append((node.left,depth+1))
                else:
                    q.append((node.right,depth+1))
                    q.append((node.left,depth+1))
        #return depth
