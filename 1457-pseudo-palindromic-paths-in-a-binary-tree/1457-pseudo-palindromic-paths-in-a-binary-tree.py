# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans=0
        self.dfs(root,0)
        return self.ans
    def dfs(self,root,a):
        if root==None:
            return
        a=a^(1<<root.val)
        if root.left==None and root.right==None:
            if a & (a-1)==0:
                self.ans+=1
        else:
            self.dfs(root.left,a)
            self.dfs(root.right,a)
       