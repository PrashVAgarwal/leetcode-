class UF:
    def __init__(self,size):
        self.par=[i for i in range(size)]
        self.rank=[1]*size
        #self.components=size
    def find(self,x):
        if x==self.par[x]:
            return x
        self.par[x]=self.find(self.par[x])
        return self.par[x]
    def union(self,a,b):
        roota=self.find(a)
        rootb=self.find(b)
        if roota!=rootb:
            if self.rank[roota]>self.rank[rootb]:
                self.par[rootb]=roota
            elif self.rank[roota]<self.rank[rootb]:
                self.par[roota]=rootb
            else:
                self.par[rootb]=roota
                self.rank[roota]+=1
            return True
        return False
            
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        uf=UF(n)
        connections.sort(key=lambda x:x[2])
        #print(connections)
        ans=0
        components=n
        for a,b,c in connections:
            if uf.union(a-1,b-1):
                components-=1
                ans+=c
            if components==1:
                return ans
        return -1
