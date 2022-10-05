# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
    
        def soln(root,string):
            if root ==None:
                return 
            elif root.left==None and root.right==None:
                string+="->"+str(root.val)
                ans.append(string[2:])
            else:
                string+="->"+str(root.val)
                soln(root.left,string)
                soln(root.right,string)
        soln(root,"")
        return ans