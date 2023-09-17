def validParentheses(s: str) -> bool:
    stack = []
    closeToOpenMap = { ")" : "(", "}" : "{", "]" : "[" }
    for c in s:
        if c in closeToOpenMap:
            if stack and stack[-1] == closeToOpenMap[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False