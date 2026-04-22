class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return len(stack) == 1