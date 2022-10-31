class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for i in range(len(matrix)):
            j=0
            temp=matrix[i][j]
            while i<len(matrix) and j<len(matrix[0]):
                if temp!=matrix[i][j]:
                    return False 
                i+=1
                j+=1
        for j in range(len(matrix[0])):
            i=0
            temp=matrix[i][j]
            while i<len(matrix) and j<len(matrix[0]):
                if temp!=matrix[i][j]:
                    return False 
                i+=1
                j+=1
        return True 