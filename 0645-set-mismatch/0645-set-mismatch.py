class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a=None
        visited=set()
        for i in nums:
            if i in visited:
                a=i
                break;
            visited.add(i)
        return [a,list(set([i for i in range(1,len(nums)+1)])-set(nums))[0]]