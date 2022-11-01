class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        
        @cache
        def soln(i,j):
            if i==len(grid):
                return j
            else:
                if grid[i][j]==1:
                    if j+1<len(grid[0]) and grid[i][j+1]==1:
                        return soln(i+1,j+1)
                    else:
                        return -1 
                else :
                    if j-1>=0 and grid[i][j-1]==-1:
                        return soln(i+1,j-1)
                    else:
                        return -1
        ans=[]
        for J in range(len(grid[0])): 
            ans.append(soln(0,J))
        return ans 
                        