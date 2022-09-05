# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict as DI
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=DI(list)
        def soln(root,col,level):
            if root:
                ans[col].append((level,root.val))
                soln(root.left,col-1,level+1)
                soln(root.right,col+1,level+1)
        soln(root,0,0)
        anss=[]
        for i in sorted(ans.keys()):
            anss.append(j[1] for j in sorted(ans[i]))
        return anss