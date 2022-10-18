class Solution:
    def countAndSay(self, n: int) -> str:
        dp=dict()
        dp[1]="1"
        def soln(n):
            if n in dp:
                return dp[n]
            else:
                a=soln(n-1)
                ans,count,last="",0,""
                for i in a:
                    if last!="" and last==i:
                        count+=1
                    else:
                        ans+=str(count)+str(last)
                        last=i
                        count=1
                ans+=str(count)+str(last)
                dp[n]=ans[1:]
                return dp[n]
        return soln(n)