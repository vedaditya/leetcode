# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def soln(root):
            if root==None:
                return ""
            else:
                l,r=soln(root.left),soln(root.right)
                if l=="" and r!="":
                    return "("+str(root.val)+"()"+r+")"
                return "("+str(root.val)+l+r+")"
        return soln(root)[1:-1]