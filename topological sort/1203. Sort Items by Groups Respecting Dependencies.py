# hard question. In this we need to do topological sort twice, once on the items and once on the groups to get the required order.
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        def topsort(adjlist,nodes,indegree): #simple topological sort implementaton
            q=deque()            
            for n in range(nodes):
                if indegree[n]==0:
                    q.append(n)
            ans=[]
            while q:
                front=q.popleft()
                ans.append(front)
                for nei in adjlist[front]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        q.append(nei)
            return ans if len(ans)==nodes else []
        
        for i in range(n): #assign groups IDs to items belonging to no group
            if group[i]==-1:
                group[i]=m
                m+=1
                
        items=[[] for _ in range(n)]
        items_indegree=[0]*n
        
        groups=[[] for _ in range(m)]
        groups_indegree=[0]*m
        
        for u in range(n):
            for v in beforeItems[u]:
                items[v].append(u) #edge from v to u as v should precede u
                items_indegree[u]+=1
                if group[u]!=group[v]:
                    groups[group[v]].append(group[u]) #group v precedes group u
                    groups_indegree[group[u]]+=1
                    
        
        topsort_items=topsort(items,n,items_indegree)
        topsort_groups=topsort(groups,m,groups_indegree)
        
        if not topsort_items or not topsort_groups:
            return []
        
        order_within_groups=defaultdict(list) 
        for i in topsort_items:
            order_within_groups[group[i]].append(i) # need to do this as we cannot simply use the groups list above as in that the items are not topologically sorted
            
        ans=[]
        for g in topsort_groups:
            ans+=order_within_groups[g]
        
        return ans
