class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1,sum2=0,0
        i,j=0,0
        result=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                result+=max(sum1,sum2)+nums1[i]
                
                i+=1
                j+=1
                sum1=0
                sum2=0
            elif nums1[i]>nums2[j]:
                sum2+=nums2[j]
                j+=1
            else:
                sum1+=nums1[i]
                i+=1
        while i<len(nums1):
            sum1+=nums1[i]
            i+=1
        while j<len(nums2):
            sum2+=nums2[j]
            j+=1
        
        result+=max(sum1,sum2)
        return result%1000000007
            