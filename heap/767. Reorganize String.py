class Solution:
    def reorganizeString(self, s: str) -> str:
        count=collections.Counter(s)
        #print(count)
        heap=[]
        for k,v in count.items():
            if v>ceil(len(s)/2): #if count of a letter > half of s then not possible to rearrange
                return ''
            heapq.heappush(heap,(-v,k)) #we first use the letters with the highest frequency so heap useful here. Greedy approach
        ans=''
        #print(heap)
        
        while heap:
            cnt,letter=heapq.heappop(heap)
            if ans=='' or ans[-1]!=letter: #if ans is empty or we have a different letter, we add it to ans
                ans+=letter
                cnt+=1
                if cnt!=0:
                    heapq.heappush(heap,((cnt,letter)))
            else:
                if not heap: #possible that heap may be empty after the first pop so need to check here
                    return ''
                cnt2,letter2=heapq.heappop(heap)
                ans+=letter2
                cnt2+=1
                if cnt2!=0:
                    heapq.heappush(heap,((cnt2,letter2)))
                heapq.heappush(heap,((cnt,letter)))
                
        return ans
