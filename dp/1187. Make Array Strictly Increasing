class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp={}  #to store memoized values
        arr2.sort() #to reduce the search time for every element
        
        def dfs(i,prev):
            if i==len(arr1):
                return 0
            if (i,prev) in dp:
                return dp[(i,prev)]
            
            cost=float('inf')
            
            if arr1[i]>prev:
                cost=dfs(i+1,arr1[i])    #in this case since already sorted so can leave as is and move to next value
                
            idx=bisect.bisect_right(arr2,prev)   # this will give the value greater than the previous value in array 2
            
            if idx<len(arr2):     #to check that the index is a valid index and not goes outside array 2
                cost=min(cost,1+dfs(i+1,arr2[idx]))   #arr2[idx] is now the previous value as we are replacing the ith value in arr1 with arr2[idx]
                
            dp[(i,prev)]=cost
            
            return cost
        
        res=dfs(0,-1)   # we are sending index, previous value. Using -1 as previous value to the first element in array 1
        
        return res if res!=float('inf') else -1
        
        
        # we have 3 cases
        1. arr1[i]>prev -> do nothing as sorted
        2. arr1[i]>prev -> still replace arr1[i] with a value greater that prev from arr2. We do this as the ith value may be very large and just replacing this value may
        reduce the number of operations needed to make the arr1 sorted.
        3. arr1[i]<prev -> in this we have to replace arr1[i] value with a value greater than prev from arr2
        
        For both 2 and 3 we need to do the same thing and we achieve this through the line
        cost=min(cost,1+dfs(i+1,arr2[idx]))
