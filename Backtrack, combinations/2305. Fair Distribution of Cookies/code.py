class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k #initializing each child with 0 cookies
        n=len(cookies)
        
        def dfs(i, children_with_0_cookies):
            if n-i < children_with_0_cookies: #if no of bags < children with 0 cookies then some children will always end up with 0 cookies so cannot lead to the minimum solution.
                return float("inf")
            
            if i == n:
                return max(children)

          # backtracking step 
            ans = float('inf') # initialize with very large value
            for j in range(k): # for each child either give him the cookie bag or not
                if children[j] == 0: # to keep track to children with 0 cookies
                    children_with_0_cookies -= 1
                children[j] += cookies[i] # give the cookie -> forward step
                
                ans = min(ans, dfs(i+1, children_with_0_cookies))
                
                children[j] -= cookies[i] # take the cookie -> backward step
                if children[j] == 0:
                    children_with_0_cookies+=1
            
            return ans
        
        return dfs(0,k)
