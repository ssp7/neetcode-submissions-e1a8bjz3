class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        
        stack = []

        for idx in range(len(s)):
            bracket = s[idx]
            if bracket in map:
                if stack and stack[-1] == map[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return len(stack) == 0