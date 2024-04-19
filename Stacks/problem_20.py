def isValid(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(")")
        elif i == "{":
            stack.append("}")
        elif i == "[":
            stack.append("]")
        elif not stack or stack.pop() != i:
            return False
        
    return not stack
