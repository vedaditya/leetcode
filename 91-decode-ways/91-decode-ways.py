class Solution:
    def numDecodings(self, s: str) -> int:
        
        dic=dict()
        def solve(s):
            if s=="":
                return 1
            elif s in dic:
                return dic[s]
            elif s[0]!="0":
                k=solve(s[1:])
                if int(s[:2])<=26 and len(s)>1:
                    dic[s]=k+solve(s[2:])
                    return dic[s]
                dic[s]=k
                return dic[s]
            dic[s]=0
            return 0
        k=solve(s)
        return k