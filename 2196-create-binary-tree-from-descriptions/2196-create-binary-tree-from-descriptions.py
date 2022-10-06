# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dic=dict()
        parent,child=set(),set()
        for i in descriptions:
            parent.add(i[0])
            child.add(i[1])
            if i[0] not in dic:
                dic[i[0]]=TreeNode(i[0])
            if i[2]==1:
                if i[1] in dic:
                    dic[i[0]].left=dic[i[1]]
                else:
                    dic[i[0]].left=TreeNode(i[1])
                    dic[i[1]]=dic[i[0]].left
            else:
                if i[1] in dic:
                    dic[i[0]].right=dic[i[1]]
                else:
                    dic[i[0]].right=TreeNode(i[1])
                    dic[i[1]]=dic[i[0]].right
            
        root=list((parent-child))
        return dic[root[0]]
        