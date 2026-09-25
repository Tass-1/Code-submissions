from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        di = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        stack = deque()
        for ch in s:
            
            if stack:
                if stack[-1] in di and  di[stack[-1]] == ch:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        if not stack:
            return True
        return False