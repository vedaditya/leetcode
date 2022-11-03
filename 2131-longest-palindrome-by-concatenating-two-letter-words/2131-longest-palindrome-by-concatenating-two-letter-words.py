from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cc=Counter(words)
        ans,temp=0,0
        for i in (words):
            rev=i[::-1]
            # print(cc,i,rev)
            if len(set(i))==1:
                if cc[i]>=2:
                    ans+=len(i)*2
                    cc[i]-=2
                elif cc[i]>=1:
                    temp=max(temp,len(i))
                    cc[i]-=1
            elif rev in cc and cc[i]>0 and cc[rev]>0:
                ans+=len(rev)*2
                cc[i]-=1
                cc[rev]-=1
            
        return ans+temp