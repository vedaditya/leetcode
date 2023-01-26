from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        hashM=defaultdict(list)
        for i in flights:
            hashM[i[0]].append([i[1],i[2]])
        # self.ans=float('inf')

        @cache
        def soln(station,k): #soln(station,cost,k):
            if station==dst:
                return 0 #self.ans=min(self.ans,cost)
                
            elif k<0:
                return float('inf')
            elif station in hashM:
                temp=float('inf')
                for i in hashM[station]:
                    tt=soln(i[0],k-1) #soln(i[0],cost+i[1],k-1)
                    temp=min(temp,tt+i[1])
                return temp
            else:
                return float('inf')
        ans=soln(src,k)
        # return self.ans if self.ans!=float('inf') else -1
        return ans if ans !=float('inf') else -1