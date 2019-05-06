while True:
    op1, op, op2  = input().split()
    op1 = int(op1)
    op2 = int(op2)

    if op == '+':
        res = op1 + op2
    elif op == '-':
        res = op1 - op2
    elif op == '*':
        res = op1 * op2
    elif op == '/':
        res = op1 / op2
    
    print('{}'.format(res))