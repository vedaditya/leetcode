# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        limit=TreeNode(-1)
        queue=[root,limit]
        parent=[]
        while queue and len(parent)<2:
            
            temp=queue.pop(0)
            if temp==limit and queue!=[]:
                queue.append(limit)
                if len(parent)==1:
                    return False 
            else:
                if temp.left:
                    queue.append(temp.left)
                    if temp.left.val==x or temp.left.val==y:
                        parent.append(temp.val)
                
                if temp.right :
                    queue.append(temp.right)
                    if temp.right.val==x or temp.right.val==y:
                        parent.append(temp.val)
                
        if len(parent)==2 and parent[0]!=parent[1]:
            return True 
        return False 
        