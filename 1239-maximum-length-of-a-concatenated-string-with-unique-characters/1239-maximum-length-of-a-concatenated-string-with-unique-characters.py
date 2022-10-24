class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        self.ans=0
        
        def combine(self,i,subString):
            if i>=len(arr):
                self.ans=max(self.ans,len(subString))
            else:
                if len(set(subString).union(set(arr[i])))==len(subString)+len(arr[i]):
                    combine(self,i+1,subString+arr[i])
                combine(self,i+1,subString)
        combine(self,0,"")
        return self.ans
                       