class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        for i,v in enumerate(nums):
            if v not in d:
                d[v]=[]
            d[v].append(i)
        print(d)
        
        ans=n
        for lst in d.values():
            t=0
            lst.append(lst[0]+n) # we add this so we need not check for the circular case i.e. last element to the first element in lst separately.
          #For circular we need to do lst[0] - lst[-1] -1 +n. This is the formula. +n to get the circular effect
            #print(lst)
            for i in range(1,len(lst)):
                t=max(t,(lst[i]-lst[i-1])//2)  # we do divide by 2 as in each second we can change both the elements adjacent to the current index eg. [1,2,3,4], 
              #for 3, we can change both 2 and 4 to 3 in one second as we see nums[i], nums[(i - 1 + n) % n], or nums[(i + 1) % n] which is nothing but i,i-1 and i+1.
          #%n if for the circular effect.
            ans=min(ans,t)
            
        return ans
