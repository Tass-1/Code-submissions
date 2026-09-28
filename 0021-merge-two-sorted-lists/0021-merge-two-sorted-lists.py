# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        p = list1
        q = list2
        head = ListNode(0)
        dum = head
        while p and q:
            pv = p.val 
            qv = q.val 
            if pv >= qv:
                dum.next=ListNode(qv)
                q=q.next
            elif qv > pv:
                dum.next=ListNode(pv)
                p = p.next
            dum = dum.next
        if p:
            dum.next = p
        if q:
            dum.next = q
        print(head)
        return head.next
