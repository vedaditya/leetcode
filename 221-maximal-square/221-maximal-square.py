class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans=0
        dp=[[0 for j in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        for i in range(1,len(matrix)+1):
            for  j in range(1,len(matrix[0])+1):
                if matrix[i-1][j-1]=="1":
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])+1
                ans=max(ans,dp[i][j])
        # print(dp)
        return ans*ans