from collections import deque
import operator
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = {"+": operator.add , "-": operator.sub, "*": operator.mul , "/": lambda a,b:int(a/b)}
        stack = deque()
        for t in tokens:
            if t in ops:
                b = int(stack.pop())
                a = int(stack.pop())
                res = ops[t](a,b)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[-1]
