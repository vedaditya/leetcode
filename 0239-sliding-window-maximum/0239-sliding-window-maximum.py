from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d=deque()
        ans=[]
        for i,val in enumerate(nums):
            while d and nums[d[-1]]<=val:
                d.pop()
            d.append(i)
            if d[0]==i-k:
                d.popleft()
            if i>=k-1:
                ans.append(nums[d[0]])
        return ans 