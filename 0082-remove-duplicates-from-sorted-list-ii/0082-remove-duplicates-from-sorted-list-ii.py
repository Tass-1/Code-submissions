# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        h = head
        t = head
        tp = None
        prev = None
        k = []
        while h:
            if prev and prev.val == h.val:
                prev.next = h.next
                h = h.next
                if prev.val not in k:
                    k.append(prev.val)
                continue
            prev = h
            h = h.next
        
        while t:
            print(k)
            print(t.val)
            if k and t.val== k[0]:
                if tp:
                    tp.next = t.next
                    t=t.next
                    k.pop(0)
                    continue
                else:
                    temp = t.next
                    t.next = None
                    t = temp
                    head = temp
                    k.pop(0)
                    continue
            tp = t
            if t:
                t = t.next
        
        return head