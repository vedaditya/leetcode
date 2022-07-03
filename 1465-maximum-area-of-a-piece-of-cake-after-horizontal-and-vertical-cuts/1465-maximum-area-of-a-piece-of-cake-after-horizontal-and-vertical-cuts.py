class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod=1000000007
        max_H=0
        pr=0
        for i in sorted(horizontalCuts):
            max_H=max(i-pr,max_H)
            pr=i
        max_H=(max(h-pr,max_H))%mod
        max_V=0
        pr=0
        for i in sorted(verticalCuts):
            max_V=max(i-pr,max_V)
            pr=i
        max_V=(max(w-pr,max_V))%mod
        return (max_V*max_H)%mod