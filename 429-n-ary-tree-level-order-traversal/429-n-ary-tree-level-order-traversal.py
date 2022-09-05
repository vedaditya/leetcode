"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import defaultdict as DI
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans=DI(list)
        
        def soln(root,level):
            if root!=None:
                ans[level].append(root.val)
                for i in root.children:
                    soln(i,level+1)
        soln(root,0)
        return list(ans.values())
        