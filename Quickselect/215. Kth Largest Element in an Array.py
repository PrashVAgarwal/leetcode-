class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def fun(nums,k):
            left,mid,right=[],[],[]
            pivot=random.choice(nums)
            for n in nums:
                if n<pivot:
                    right.append(n)
                elif n>pivot:
                    left.append(n)
                else:
                    mid.append(n)
            if k<=len(left):
                return fun(left,k)
            if k>len(left)+len(mid):
                return fun(right,k-len(left)-len(mid))
            return pivot
        return fun(nums,k)

  #quickselect gives average runtime complexity O(n).
