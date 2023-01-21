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
    
def is_operator(x):
    if x == '+':
        return 1
    elif x == '-':
        return 2
    elif x == '*':
        return 3
    elif x == '/':
        return 4
    
def EvalutePrefix(expression):
    operandStack = []
    lst = expression.split()
    lst = lst[::-1]
    for i in lst:
        o = is_operator(i)
        if o != 1 and o != 2 and o != 3 and o != 4:
            push(operandStack, int(i))
        else:
            f = float(top(operandStack))
            pop(operandStack)
            s = float(top(operandStack))
            pop(operandStack)
            if o == 1:
                r = f + s
            elif o == 2:
                r = f - s
            elif o == 3:
                r = f * s
            elif o == 4:
                r = f / s
            push(operandStack, int(r))
    return (top(operandStack))
print(EvalutePrefix(expression))
