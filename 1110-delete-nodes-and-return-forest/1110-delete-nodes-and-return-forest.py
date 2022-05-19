# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans=[]
        
        
        def dfs(root,fl):
            if root==None:
                return 
            if root.val in to_delete:
                dfs(root.left,0)
                dfs(root.right,0)
                return None
            else:
                if fl==0:
                    ans.append(root)
                root.right=dfs(root.right,1)
                root.left=dfs(root.left,1)
                return root
        if root.val not in to_delete:
            ans.append(root)
        dfs(root,1)
        return ans