class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_={}
        for i in range(len(nums)):
            if nums[i] in dict_:
                if abs(dict_[nums[i]]-i)<=k:
                    return True 
            dict_[nums[i]]=i
        return False 
                