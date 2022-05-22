# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev=[(TreeNode(float("-inf")))]
        self.replace=[]
        self.soln(root)
        self.replace[0][0].val,self.replace[-1][-1].val=self.replace[-1][-1].val,self.replace[0][0].val
        
    def soln(self,root):
        if root==None :
            return 
        self.soln(root.left)
        if root.val<self.prev[0].val:
            self.replace.append([self.prev[0],root])
        self.prev=[root]
        self.soln(root.right)
            
        