class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        for i in range(len(data)):
            if data[i]==255:
                return False 
            data[i]='{:08b}'.format(data[i])
        k=0
        for i in data:
            if k==0:
                ind=i.index("0")
                if ind==0:
                    continue
                if ind==1 or ind>4:
                    return False 
                k=ind-1
            else: 
                if i[:2]=="10":
                    k-=1
                else :
                    
                    return False  

        return True if k==0 else False 
                
            