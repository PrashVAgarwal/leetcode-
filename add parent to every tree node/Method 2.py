par={root:None}
        
st=[root]

while st:
    top=st.pop()
    
    if top.left:
        par[top.left]=top
        st.append(top.left)
    if top.right:
        par[top.right]=top
        st.append(top.right)

  #does not modify the node data structure
