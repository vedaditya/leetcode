class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices==sorted(prices):
            return prices[-1]-prices[0]
        
        def max_2nd(i):
            print("ggg")
            j=i
            anss=[0,0]
            for J in range(i+1,len(prices)):
                if prices[J]<prices[j]:
                    j=J
                else:
                    if anss[0]<=prices[J]-prices[j]:
                        anss=[prices[J]-prices[j],j]
            print(anss)
            return anss 
        
        ans=0
        min1=float("inf")
        kk=max_2nd(1)
        
        for i in range(len(prices)):
            if prices[i]<min1:
                min1=prices[i]
            else:
                if i>=kk[-1] and kk[0]!=0:  
                    kk=max_2nd(i+1)
                ans=max(ans,prices[i]-min1+kk[0])
        return ans 