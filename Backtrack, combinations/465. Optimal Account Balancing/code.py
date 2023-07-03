class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        d = {}
        #getting each persons net debt. -ve if they owe, +ve if they are owed
        for a,b,amt in transactions:
            if b not in d:
                d[b]=0
            if a not in d:
                d[a]=0
            d[b]-=amt
            d[a]+=amt
            
        print(d)
        #just keeping the non-zero debts in a list as no need to consider 0 debts as no transactions needed to settle them
        netlist = [amt for amt in d.values() if amt]
        print(netlist)
        
        n=len(netlist)
        
        def fun(cur):
            #going to the next index if current index's value is 0 as no transaction needed for this index
            while cur<n and netlist[cur]==0:
                cur+=1
            #base case
            if cur==n:
                return 0
            #variable to store the result i.e. no of transactions needed. In backtracking we need to declare such variables before backtracking begins
            cost= float('inf')
            for nxt in range(cur+1,n):
                #only transfer debt if sign of current debt and next debt is opposite. This is to improve runtime
                if netlist[nxt]*netlist[cur]<0:
                    #backtrack steps
                    netlist[nxt]+=netlist[cur]
                    cost=min(cost,1+fun(cur+1))
                    netlist[nxt]-=netlist[cur]
            return cost
        return fun(0)
