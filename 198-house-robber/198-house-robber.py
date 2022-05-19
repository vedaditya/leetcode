class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        
        def soln(i):
            if len(nums)==i:
                return 0
            if len(nums)-1==i:
                return nums[i]
            if i not in dp:
               
                dp[i]=max(nums[i]+soln(i+2),soln(i+1))
            return dp[i]
        return soln(0)
        
    
            