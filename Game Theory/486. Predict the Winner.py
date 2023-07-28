class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        l=0
        r=len(nums)-1
        
        @lru_cache(None)
        def fun(l,r):
            if l==r:
                return nums[l]
            return max(nums[l]-fun(l+1,r), nums[r]-fun(l,r-1)) #main line. Since we are only concerned with player 1's score, this will return the max delta score
          #(player1-player2) player1 can get when he chooses the leftmost or rightmost element respectively.
        
        return fun(0,r)>=0
