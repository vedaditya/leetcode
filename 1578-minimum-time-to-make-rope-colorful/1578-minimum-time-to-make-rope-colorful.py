class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans=0
        tt=neededTime[0]
        sum_=tt
        for i in range(1,len(colors)):
            if colors[i]==colors[i-1]:
                tt=max(tt,neededTime[i])
                sum_+=neededTime[i]
            else:
                ans+=(sum_-tt)
                tt=neededTime[i]
                sum_=tt
                # print(ans,sum_,tt,i)
        if colors[-1]==colors[-2]:
            ans+=(sum_-tt)
        return ans 