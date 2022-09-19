from collections import defaultdict as D
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mapp=D(list)
        for i in paths:
            i=i.split(" ")
            for j in range(1,len(i)):
                text=""
                st=i[j].index("(")+1
                t=st
                while i[j][st]!=")":
                    text+=i[j][st]
                    st+=1
                ans=i[0]+"/"+i[j][:t-1]
                mapp[text].append(ans)
        ans=[]
        for j in mapp.values():
            if len(j)>1:
                ans.append(j)
        return ans 