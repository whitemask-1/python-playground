def evalRPN(tokens: list(str)) -> int:
    op_stack = []
    for c in tokens:
        if c == "+":
            x = op_stack.pop()
            y = op_stack.pop()
            op_stack.append(y + x)
        elif c == "-":
            x = op_stack.pop()
            y = op_stack.pop()
            op_stack.append(y - x)
        elif c == "*":
            x = op_stack.pop()
            y = op_stack.pop()
            op_stack.append(y * x)
        elif c == "/":
            x = op_stack.pop()
            y = op_stack.pop()
            op_stack.append(int(y / x))
        else:
            op_stack.append(int(c))

    return op_stack[0]

token_list = ["2","1","+","3","*"]

print(evalRPN(token_list))
