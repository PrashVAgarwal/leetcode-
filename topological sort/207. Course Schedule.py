class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses #initialize all indegrees as 0
        adj=[[] for _ in range(numCourses)]
        
        for course, prereq in prerequisites: #create an adjacency list and increment indegree of nodes accordingly
            indegree[course]+=1
            adj[prereq].append(course)
            
        q=deque()
        for i in range(numCourses): #get all the nodes with indegree 0 as the starting points
            if indegree[i]==0:
                q.append(i)
        
        visitcount=0
        
        while q:
            front=q.popleft()
            visitcount+=1
            for nei in adj[front]: #remove the 0 indegree nodes and reduce the indegree count by 1 for all the nodes that have this node coming to them
                indegree[nei]-=1
                if indegree[nei]<=0: #if a node's indegree reaches 0, add it to the queue
                    q.append(nei)
        
        return visitcount==numCourses #if all the nodes do have an indegree=0 then there is a cycle
