class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=""
        kk=2*k
        for i in range(0,len(s),kk):
            ss=s[i:i+kk]
            ans+=ss[:k][::-1]
            ans+=ss[k:]
        return ans 