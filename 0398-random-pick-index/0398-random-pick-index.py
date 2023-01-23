class Solution:

    def __init__(self, nums: List[int]):
        self.dict=defaultdict(list)
        for i in range(len(nums)):
            self.dict[nums[i]].append(i)
        # print(self.dict)
    def pick(self, target: int) -> int:
        return random.choice(self.dict[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)