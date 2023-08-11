class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        print(dp)
        for c in coins:
            for i in range(amount+1):
                if i-c<0: #i-c should be>=0 as our dp starts from 0
                    continue
                dp[i]=min(dp[i],dp[i-c]+1)
        print(dp)
        return dp[-1] if dp[-1]!=amount+1 else -1
