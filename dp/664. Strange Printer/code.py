class Solution:
    def strangePrinter(self, s: str) -> int:
        memo={}
        
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==j:
                return 1
            turns=float('inf')
            for k in range(i,j):
                turns=min(turns ,dp(i,k) + dp(k+1,j))
            memo[(i,j)] = turns if s[i]!=s[j] else turns-1 #edge case like aa is split at a|a so we will return 2 turns but we just need 1 turn to type this string
            return memo[(i,j)]
        
        return dp(0,len(s)-1)
            
