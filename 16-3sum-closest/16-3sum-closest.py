def twosummin(nums,target,start):
    end=len(nums)-1
    ans=nums[start]+nums[end]
    while start<end:
        sum_=nums[start]+nums[end]
        if sum_==target:
            ans=sum_
            break
        else:
            if abs(sum_-target)<abs(ans-target):
                ans=sum_
            if sum_>target:
                end-=1
            else:
                start+=1
    return ans

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=999999999
        for i in range(len(nums)-2):
            kk=twosummin(nums,target-nums[i],i+1)
            print(kk,nums[i],i)
            sum_=kk+nums[i]
            if sum_==target:
                ans=sum_
                break
            else:
                if abs(sum_-target)<abs(ans-target):
                    ans=sum_
        return ans
            