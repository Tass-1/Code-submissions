class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        result = 0
        sign = 1
        
        for char in s:
            if char.isdigit():
                current_num = (current_num * 10) + int(char)
            elif char == '+':
                result += sign * current_num
                sign = 1
                current_num = 0
            elif char == '-':
                result += sign * current_num
                sign = -1
                current_num = 0
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * current_num
                current_num = 0
                result *= stack.pop()
                result += stack.pop()
                
        result += sign * current_num
        return result