class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        
        while curr:
            next_level_head = None
            next_level_tail = None
            
            while curr:
                if curr.left:
                    if next_level_tail:
                        next_level_tail.next = curr.left
                    else:
                        next_level_head = curr.left
                    next_level_tail = curr.left
                    
                if curr.right:
                    if next_level_tail:
                        next_level_tail.next = curr.right
                    else:
                        next_level_head = curr.right
                    next_level_tail = curr.right
                    
                curr = curr.next
                
            curr = next_level_head
            
        return root