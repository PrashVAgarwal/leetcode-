# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        st=[]
        st.append((root,1))
        ans=0
        if not root:
            return 0
        while st:
            node,depth=st.pop()
            if node.left==None and node.right==None:
                #print(node.val,depth)
                ans=max(ans,depth)
            elif node.left==None:
                st.append((node.right,depth+1))
            elif node.right==None:
                st.append((node.left,depth+1))
            else:
                st.append((node.right,depth+1))
                st.append((node.left,depth+1))
        return ans
