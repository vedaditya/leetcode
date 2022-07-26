# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def soln(root,p,q):
            if root==None :
                return False 
            right=soln(root.right,p,q)  
            left=soln(root.left,p,q)
            if root.val==p.val or root.val==q.val:
                if left or right:
                    return root
                return True 
            
            if left and right :
                return root
            elif left:
                return left
            else :
                return right 
        return soln(root,p,q)