class Solution:
    def rob(self, nums: List[int]) -> int:
        one=0
        two=0
        for i in nums:
            newnum=max(one+i,two)
            one=two
            two=newnum
        return two