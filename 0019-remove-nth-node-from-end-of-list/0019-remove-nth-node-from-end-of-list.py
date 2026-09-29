# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        c= 0
        h = head
        t = head
        while h:
            c += 1
            h = h.next
        if c == 1:
            return None
        rm = c-(n-1)
        k = 1
        while t:
            if k == rm:
                if k == 1:
                    return t.next
                else:
                    prev.next = t.next
                break
            k += 1
            prev = t
            t=t.next
        return head