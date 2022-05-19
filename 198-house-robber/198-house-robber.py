class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        if len(nums)==1:
            return nums[0]
        
        nums[1]=max(nums[1],nums[0])
        for i in range(2,len(nums)):
            nums[i]=max(nums[i-1],nums[i-2]+nums[i])
        return nums[-1]