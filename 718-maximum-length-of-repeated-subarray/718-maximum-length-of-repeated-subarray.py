class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        first=[0 for i in range(len(nums2))]
        ans=0
        for i in range(len(nums1)) :
            curr=[]
            maxx=0
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    curr.append((first[j-1]if j>0 else 0)+1)
                    maxx=max(maxx,curr[-1])
                else:
                    curr.append(0)
            ans=max(ans,maxx)
            first=curr.copy()
        return ans