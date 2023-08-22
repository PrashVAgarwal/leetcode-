class UF:
    def __init__(self,size):
        self.par=[i for i in range(size)]
        self.rank=[1]*size
    def find(self,x):
        if x==self.par[x]:
            return x
        self.par[x]=self.find(self.par[x])
        return self.par[x]
    def union(self,a,b):
        roota,rootb=self.find(a),self.find(b)
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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        uf=UF(n)
        e=[]
        for i,ne in enumerate(edges):#adding index with the edges
            e.append((i,ne[0],ne[1],ne[2]))
        #print(e)
        e.sort(key=lambda x:x[3])
        #print(e)
        crit=[]
        pseudo=[]
        mincost=0
        components=n
        #mstset=set()
        for i,a,b,c in e:
            if uf.union(a,b):
                mincost+=c
                components-=1
                #mstset.add(i)
            if components==1:
                break
        #print(mincost)
        
        for i in range(len(e)):
            exclude=e[i]
            l=e[:i]+e[i+1:]
            #print(l)
            #print(exclude)
            cost=0
            components=n
            uf=UF(n)
            for j,a,b,c in l:
                if uf.union(a,b):
                    cost+=c
                    components-=1
                    #mstset.add(j)
                if components==1:
                    break
            #print(exclude,cost)
            if cost>mincost or components!=1:
                crit.append(exclude[0])
                continue
            uf=UF(n)
            cost=exclude[3]
            uf.union(exclude[1],exclude[2])
            for j,a,b,c in l:
                if uf.union(a,b):
                    cost+=c
                    components-=1
            if cost==mincost:
                pseudo.append(exclude[0])
        #print([crit,pseudo])
        '''for i in range(len(crit)):
            if crit[i] not in mstset:
                del crit[i]
        for i in range(len(pseudo)):
            if pseudo[i] not in mstset:
                del pseudo[i]'''
        return [crit,pseudo]
            
