class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        #sorting according to start time
        events.sort()
        n=len(events)
        #keeping a list of start times to help search for the next event we can attend
        starts=[start for start,e,v in events]
        #2D dp array
        dp=[[-1]*(k+1) for _ in range(n)]
        
        def fun(pos,k):
            #if pos==n means no more events left or k==0 means cannot attend any more events
            if pos==n or k==0:
                return 0
            #if value present in our dp then simply return that (memoization)
            if dp[pos][k]!=-1:
                return dp[pos][k]
            
            #using binary search to get the next possible event we can attend
            next_pos=bisect_right(starts,events[pos][1])
            #simple knapsack type function
            #either do not take the current event so simply go to the next event in line (pos+1)
            #or attend the current event, so add its value and go to the next possible event (next_pos)
            dp[pos][k]=max(fun(pos+1,k), events[pos][2]+fun(next_pos,k-1))
            return dp[pos][k]
        
        return fun(0,k)
