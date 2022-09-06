# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return None

        left,right=self.pruneTree(root.left),self.pruneTree(root.right)
        root.left,root.right=None, None 
        if left:
            root.left=left
        if right:
            root.right =right 
        return root if (left or right or root.val) else None 
        
        # if left and right:
        #     root.left=left
        #     root.right=right
        #     return root
        # elif left:
        #     root.right=None
        #     root.left=left
        #     return root
        # elif right:
        #     root.left=None
        #     root.right=right
        #     return root
        # else:
        #     root.left=None
        #     root.right=None
        #     return root if root.val==1 else None 
        