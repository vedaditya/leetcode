from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans=[]
        ccdict=Counter(words)
        freq=sorted(ccdict.values())[-k]
        for key,value in ccdict.items():
            if value >= freq:
                ans.append(key)

        return sorted(ans,key=lambda i:(-ccdict[i],i) )[:k]