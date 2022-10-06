# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i,j=0,n+1
        while j-i>1:
            mid=(i+j)//2
            if isBadVersion(mid):
                j=mid
            else:
                i=mid
        return j 