# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans=0
        self.dfs(root,[0 for i in range(10)])
        return self.ans
    def dfs(self,root,a):
        if root==None:
            return
        elif root.left==None and root.right==None:
            aa=a.copy()
            aa[root.val]+=1
            kk=0
            for i in aa:
                if i%2!=0:
                    kk+=1
            if kk<=1:
                self.ans+=1
        else:
            aa=a.copy()
            aa[root.val]+=1
            self.dfs(root.left,aa)
            self.dfs(root.right,aa)
       