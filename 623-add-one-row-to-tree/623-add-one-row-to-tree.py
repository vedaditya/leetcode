# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            ans=TreeNode(val)
            ans.left=root
            return ans 
        def soln(root,depth):
            if depth<1 or root==None:
                return 
            if depth ==1:
                left=root.left
                right=root.right
                root.left=TreeNode(val)
                root.right=TreeNode(val)
                root.left.left=left
                root.right.right=right
            else:
                soln(root.left,depth-1)
                soln(root.right,depth-1)
        soln(root,depth-1)
        return root 