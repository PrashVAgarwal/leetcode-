def dfs(node,par):
            if not node:
                return
            node.par=par
            dfs(node.left,node)
            dfs(node.right,node)
            
        dfs(root,None)

#this modifies the data structure of the node
