class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        st,en=0,len(nums)-1
        
        while en>=st:
            mid=(en+st)//2
            if nums[en]==nums[st]==target:
                return [st,en]
            elif nums[mid]!=target:
                if nums[mid]>target and en>mid:
                    en=mid-1
                elif nums[mid]<target and st<mid:
                    st=mid+1
                        
            if nums[st]!=target:
                st+=1
            if nums[en]!=target:
                en-=1
            #print(st,en)
        return [-1,-1]