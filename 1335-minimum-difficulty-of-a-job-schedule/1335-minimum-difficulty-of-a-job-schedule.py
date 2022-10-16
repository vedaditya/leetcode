class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        @cache
        def solve(i,j):
            if j==1 and i<len(jobDifficulty):
                return max(jobDifficulty[i:])
            
            else:
                ans=float("inf")
                max_=0
                for k in range(i,len(jobDifficulty)):
                    max_=max(max_,jobDifficulty[k])
                    ans=min(ans,max_+solve(k+1,j-1))
                    # print(ans,i,j,max_)
                return ans
            
        ans= solve(0,d) 
        return ans if ans!=float("inf") else -1