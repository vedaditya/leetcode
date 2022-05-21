class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp={0:0}
        def min_(val):
            if val in dp:
                return dp[val]
            if val in coins:
                dp[val]=1
                return 1
            dp[val]=float("inf")
            for i in coins:
                if val>i:
                    dp[val]=min(dp[val],1+min_(val-i))
            return dp[val]
        min_(amount)
        print(dp,amount)
        return dp[amount] if dp[amount]!=float("inf") else -1
        