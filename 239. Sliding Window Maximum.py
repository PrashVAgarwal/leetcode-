# Here we use a monotonic deque. A monotonic datastructure is one which keeps the elements in sorted order always.
# Here we only keep the largest elements in the queue as within a given k range, one of these will be the max value

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        q=deque()
      #we push the largest element indexes from the first k elements in the queue
        for i in range(k):
            if not q:
                q.append(i)
            while q and nums[q[-1]]<=nums[i]: #we pop elements from the end of the queue which are smaller than the current element as they cannot be the max value.
                q.pop()
            q.append(i)
        ans.append(nums[q[0]]) #always push the the first element in the result array as we are maintaining a decending queue so the largest value is always at index 0 in queue.
        
        for i in range(k,len(nums)):
            #print(i)
            #print(q)
            while q and nums[q[-1]]<=nums[i]:
                q.pop()
            q.append(i)
            #print(q)
            while q and q[0]<=i-k: #remove elements from the front of the queue if they are out of k range
                q.popleft()
            #print(q)
            ans.append(nums[q[0]])
        return ans
