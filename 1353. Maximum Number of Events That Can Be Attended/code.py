class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap=[]
        day=1  #keeps track of which day we are on
        ans=0
        i=0
        
        while i<len(events) or heap:
            if not heap:   #if heap is empty we assign the first start day as our current day
                day=events[i][0]
            
            #keep adding events happening on current day to our heap
            while i<len(events) and events[i][0]<=day: 
                heapq.heappush(heap,events[i][1])
                i+=1
            
            #remove events which cannot be attended as their end day<current day
            while heap and heap[0]<day:
                heapq.heappop(heap)
            
            #if heap not empty, attend the earliest ending event (min heap so at top)
            if heap:
                ans+=1
                heapq.heappop(heap)
                day+=1
                
        return ans
