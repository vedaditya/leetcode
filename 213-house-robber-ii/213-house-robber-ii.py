class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.solver(nums[1:]),self.solver(nums[:-1]))
    def solver(self,nums):
            one=0
            two=0
            for i in nums:
                newnum=max(one+i,two)
                one=two
                two=newnum
            return two