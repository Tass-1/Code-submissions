# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left == right:
            return head
        c = 1
        k = []
        h = head
        while h:
            k.append(h.val)
            h = h.next
        left -= 1
        right -= 1
        while left < right:
            temp = k[left]
            k[left] = k[right]
            k[right] = temp
            left += 1
            right -= 1
        temp = ListNode(k[0])
        dum = temp
        for i in range(1,len(k)):
            dum.next = ListNode(k[i])
            dum = dum.next
        return temp