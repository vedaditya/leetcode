from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for i in strs:
            key="".join(sorted(list(i)))
            a[key].append(i)
        return a.values()
        