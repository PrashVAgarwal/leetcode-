# here to distinguish between left and right portions, we use 0 and 1. 0 for left portion and 1 for right portion so in case of tie, element is picked from left as lower 0 < 1.
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        for i in range(candidates):
            heapq.heappush(heap, (costs[i], 0))
                        
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            heapq.heappush(heap, (costs[i], 1))
        
        l = candidates
        r = len(costs) - candidates - 1
        ans = 0
        
        while k > 0:
            val, indx = heapq.heappop(heap)
            ans += val
            
            if l <= r:
                if indx == 0:
                    heapq.heappush(heap, (costs[l], 0))
                    l += 1
                else:
                    heapq.heappush(heap, (costs[r], 1))
                    r -= 1
            k -= 1
        return ans
