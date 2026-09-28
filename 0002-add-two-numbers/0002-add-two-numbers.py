# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        p = l1
        q = l2
        head = ListNode(0)
        temp = head
        carry = 0
        while p or q:
            pv = p.val if p else 0
            qv = q.val if q else 0
            s = pv+qv+carry
            if s >= 10:
                m = s%10
                temp.next = ListNode(m)
                carry = 1
            else:
                temp.next = ListNode(s)
                carry = 0
            temp = temp.next
            p = p.next if p else None
            q = q.next if q else None
        if carry == 1:
            temp.next = ListNode(1)
        print(temp)
        print(head)
        return head.next