class Solution:
    def trap(self, height: List[int]) -> int:
        total,lmax,rmax=0,0,0
        i,j=0,len(height)-1
        while i<j:
            if height[i]<height[j]:
                
                if height[i]>=lmax:
                    lmax=height[i]
                else:
                    total+=lmax-height[i]
                i+=1
            else:
                if height[j]>=rmax:
                    rmax=height[j]
                else :
                    total+=rmax-height[j]
                j-=1
        return total 