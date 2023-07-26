class Solution:
    def parseTernary(self, e: str) -> str:
        
        while len(e)!=1:
            qindex=len(e)-1
            
            while e[qindex]!='?':
                qindex-=1
                
            if e[qindex-1]=='T':
                val=e[qindex+1]
            else:
                val=e[qindex+3]
              
            #so here we are changing the expression "e" itself and so its length changes as well
            e=e[:qindex-1] + val + e[qindex+4:]
            
        return e
