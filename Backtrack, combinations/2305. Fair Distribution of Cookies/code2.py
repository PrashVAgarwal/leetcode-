# can optimize further by keeping a set of seen states
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        n=len(cookies)
        
        def dfs(i, children_with_0_cookies):
            seen = set()
            if n-i < children_with_0_cookies:
                return float("inf")
            
            if i == n:
                return max(children)
            
            ans = float('inf')
            
            for j in range(k):
                if children[j] in seen:
                    continue
                seen.add(children[j])
                if children[j] == 0:
                    children_with_0_cookies -= 1
                children[j] += cookies[i]
                                                
                ans = min(ans, dfs(i+1, children_with_0_cookies))
                
                children[j] -= cookies[i]
                if children[j] == 0:
                    children_with_0_cookies+=1
            
            return ans
        
        return dfs(0,k)
