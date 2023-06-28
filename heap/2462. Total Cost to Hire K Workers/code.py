class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        #heapify left and right portions
        leftheap = costs[:candidates]
        rightheap = costs[max(candidates, len(costs) - candidates):]
        heapify(leftheap)
        heapify(rightheap)
        leftptr = candidates
        rightptr = len(costs) - candidates -1
        
        ans = 0
        
        while k > 0:
            if not rightheap or leftheap and leftheap[0]<=rightheap[0]:
                ans += heapq.heappop(leftheap)
                if leftptr <= rightptr:
                    heapq.heappush(leftheap, costs[leftptr])
                    leftptr += 1
            else:
                ans += heapq.heappop(rightheap)
                if leftptr <= rightptr:
                    heapq.heappush(rightheap, costs[rightptr])
                    rightptr -= 1
            k -= 1
        return ans
