class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=9999999999
        sum_=0
        len_=0
        i,j=0,0
        while sum_>=0 and j<len(nums):
            if sum_<target:
                len_+=1
                sum_+=nums[j]
                j+=1
            else:
                ans=min(ans,len_)
                len_-=1
                sum_-=nums[i]
                i+=1
        
        while sum_>=target:
            ans=min(ans,len_)
            len_-=1
            sum_-=nums[i]
            i+=1
            
        return ans if ans!=9999999999 else 0