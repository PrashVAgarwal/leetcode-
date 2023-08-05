# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp={}
        
        def fun(lower, upper):
            if (lower,upper) in dp:
                return dp[(lower,upper)]
            if lower>upper:
                return [None]
            if lower==upper: #i.e. just one node
                return [TreeNode(lower)]
            
            ans=[]
            for i in range(lower,upper+1):
                #i is the current node so we see left and right of it
                left=fun(lower,i-1)
                right=fun(i+1,upper)
                
                for l in left:
                    for r in right:
                        ans.append(TreeNode(i,l,r))
                        
            dp[(lower,upper)]=ans
            return dp[(lower,upper)]
        
        return fun(1,n)
