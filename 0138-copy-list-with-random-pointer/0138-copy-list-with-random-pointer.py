"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = Node(0)
        dummy = temp
        t = temp
        di = {}
        tra = set()
        h = head
        while h:
            if h in di or h in tra:
                dummy.next = di[h]
            else:
                dummy.next = Node(h.val)
                di[h] = dummy.next
                tra.add(h)
            if h.random in di or h.random in tra:
                dummy.next.random = di[h.random]
            else:
                dummy.next.random = Node(h.random.val) if h.random else None
                if h.random:
                    tra.add(h.random)
                    di[h.random] = dummy.next.random
            h = h.next
            dummy = dummy.next
        print(t)
        return t.next