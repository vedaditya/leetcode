# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp=head
        delete=head
        k=0
        while k<n:
            temp=temp.next
            k+=1
        if temp!=None:   
            while temp.next!=None:
                temp=temp.next
                delete=delete.next
                k+=1
        else:
            return head.next
        delete.next=delete.next.next
        return head
        