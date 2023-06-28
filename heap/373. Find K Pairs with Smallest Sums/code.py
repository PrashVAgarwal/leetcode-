class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        ans = []
        lennums1 = len(nums1)
        lennums2 = len(nums2)
        heapq.heappush(heap, (0, 0, 0))
        st = set()
        
        while heap and len(ans) < k:
            _, i ,j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            
            if (i+1) < lennums1 and (i+1,j) not in st:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
                st.add((i+1,j))
            if (j+1) < lennums2 and (i,j+1) not in st:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
                st.add((i,j+1))
        
        return ans
