# Application of stack for postfix evaluation
def postfix(expr):
    stack = []
    for i in expr:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(b - a)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(b // a)
    return stack.pop()
eq = input("Enter an expression: ").split()
print(postfix(eq))