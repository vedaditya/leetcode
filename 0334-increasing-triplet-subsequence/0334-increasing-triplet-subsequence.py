class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_=float("inf")
        max_=float("inf")
        for i in nums:
            if i==min_:
                continue
            elif i<min_:
                min_=i
            elif i<max_:
                max_=i
            elif min_!=float("inf") and max_!=float("inf") and i>max_:
                return True 
        return False 