# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue=[root,-1]
        sum_=[]
        ans=[]
        while queue!=[]:
            a=queue.pop(0)
            if a==-1 :
                ans.append(sum(sum_)/len(sum_))
                sum_=[]
                if queue!=[]:
                    queue.append(-1)
            else:
                sum_.append(a.val)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
        return ans 