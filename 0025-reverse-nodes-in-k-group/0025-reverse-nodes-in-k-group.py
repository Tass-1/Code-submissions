# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        h = head
        m = []
        while h:
            m.append(h.val)
            h = h.next
        
        left = 0
        right = k-1
        while right < len(m):
            l = left
            r = right
            print(l , r)
            while l < r:
                temp = m[l]
                m[l] = m[r]
                m[r] = temp
                l += 1
                r -= 1
            left = right + 1
            right += k
        
        temp = ListNode(m[0])
        dum = temp
        for i in range(1,len(m)):
            dum.next = ListNode(m[i])
            dum = dum.next
        print(m)
        return temp