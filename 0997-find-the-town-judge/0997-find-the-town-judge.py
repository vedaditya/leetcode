from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        Map=defaultdict(set)
        for i in trust:
            Map[i[0]].add(i[1])
        if len(Map)!=n-1:
            return -1 
        for i in range(1,n+1):
            if i not in Map:
                break;
        for j in Map:
            if i not in Map[j]:
                return -1
        return i
        