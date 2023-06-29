Simple BFS traversal to find the shortest path collecting all the keys.

Trick - In the queue save the state as well as having a key changes the state and we can travel back the same path as now the state has changed

VERY IMPORTANT - Earlier I was updating keys as follows:
elif 'a'<=grid[ni][nj]<='z':
    keys += grid[ni][nj]
    q.append((ni,nj,keys+grid[ni][nj],steps+1))
    seen.add((ni,nj,keys))

this will cause the value of keys to be updated for the current iteration and give incorrect results



Correct way is:
elif 'a'<=grid[ni][nj]<='z':
    q.append((ni,nj,keys+grid[ni][nj],steps+1))
    seen.add((ni,nj,keys))

this way keys is not updated for the current iteration but its updated value is inserted into the queue
