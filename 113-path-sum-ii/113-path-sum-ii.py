# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root== None :
            return []
        ans=[]
        def soln(root,target):
            if root !=None :
                if root.left==None and root.right==None  :
                    if sum(root.val)==target:
                        ans.append(root.val) 
                if root.left !=None :
                    root.left.val=root.val+[root.left.val]
                if root.right!=None :
                    root.right.val=root.val+[root.right.val]
                soln(root.right,target)   
                soln(root.left,target)
            
        root.val=[root.val]
        soln(root,targetSum)
        return ans 