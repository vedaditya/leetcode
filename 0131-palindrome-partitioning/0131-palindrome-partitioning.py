class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.ans=[]
        def helper(s,temp):
            
            if s=="":
                self.ans.append(temp)
            else:
                # tt=temp.copy()
                # tt.append(s[0])
                # helper(tt,s[1:])
                tempS=''
                for I in range(len(s)):
                    i=s[I]
                    tempS+=i
                    if tempS==tempS[::-1]:
                        tt=temp.copy()
                        tt.append(tempS)
                        helper(s[I+1:],tt)
        helper(s,[])
        return self.ans 