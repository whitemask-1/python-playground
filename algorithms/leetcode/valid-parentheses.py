def validParentheses(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    stack = [_ for _ in s]
    valid_tuples = [("(",")"), ("{", "}"), ("[", "]")]

    while stack:
       
        current = stack[0]
        matching = stack[-1]
        
        if (current, matching) not in valid_tuples:
            return False

        stack.pop(0)
        stack.pop(-1)

    return True


def isValid(s: str) -> bool:
    stack = []
    closeToOpen = {")" : "(", "]" : "[","}" : "{" }

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                print(stack)
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False

print(isValid("({})"))
