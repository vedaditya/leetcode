from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or s=="":
            return ""
        dict_t,dict_w,formed=Counter(t),defaultdict(int),0
        left,right=0,0
        ans=[float("inf"),None,None]
        
        while right <len(s):
            c=s[right]
            dict_w[c]+=1
            if c in dict_t and dict_t[c]==dict_w[c]:
                formed+=1
            while left<=right and formed==len(dict_t):
                c=s[left]
                if right-left+1<ans[0]:
                    ans=[right-left+1,left,right]
                dict_w[c]-=1
                if c in dict_t and dict_t[c]>dict_w[c]:
                    formed-=1
                left+=1
            right+=1
        return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]
        
            