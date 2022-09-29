class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minheap=[]
        ans=[]
        for i in range(len(arr)):
            diff = abs(x-arr[i])
            heapq.heappush(minheap,[diff,arr[i]])
        for i in range(k):
            diff,val=heapq.heappop(minheap)
            ans.append(val)
        ans.sort()
        return ans