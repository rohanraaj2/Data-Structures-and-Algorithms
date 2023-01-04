expression = input()
def push (lst, item):
    lst.append(item)
    
def pop(lst):
    return(lst.pop())
    
def top(lst):
    return(lst[-1])

def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False

def Infix_to_Postfix(expression):
    op_stack = []
    out = []
    s = ''
    infix = expression.split()
    p = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}
    for i in infix:
        if i.isalpha() == True:
            out.append(i)
        elif i == '(' or is_empty(op_stack) == True:
            push(op_stack, i)
        else:
            if i == ')':
                while is_empty(op_stack) == False and top(op_stack) != '(':
                    out.append(pop(op_stack))
                pop(op_stack)
            else:
                while is_empty(op_stack) == False and (p[top(op_stack)] >= p[i]):
                    out.append(pop(op_stack))
                push(op_stack, i)
    while is_empty(op_stack) == False:
        out.append(pop(op_stack))
    for j in out:
        s += j + ' '
    return s

print(Infix_to_Postfix(expression))
