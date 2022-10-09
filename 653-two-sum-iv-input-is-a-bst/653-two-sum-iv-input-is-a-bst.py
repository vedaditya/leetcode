# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def search(root,target):
            if root==None:
                return False 
            elif  root.val==target and root!=self.temp:
                return True 
            elif root.val>target:
                return search(root.left,target)
            else:
                return search(root.right,target)
        
        def dfs(head,root):
            if root ==None:
                return False 

            target=k-root.val
            self.temp=root
            if search(head,target):
                return True 
            else:
                return dfs(head,root.left) or dfs(head,root.right )
        return dfs(root,root)