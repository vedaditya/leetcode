# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t1,t2=head,head
        if head.next==None:
            return None
        elif head.next.next==None:
            head.next=None
            return head
        while t2 and t2.next:
            t1=t1.next
            t2=t2.next.next
        
        t1.val=t1.next.val
        t1.next=t1.next.next
        
        return head