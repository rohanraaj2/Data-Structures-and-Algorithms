exp = input()
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
    
def postfixEval(exp):
    lst = exp.split()
    n = []
    for i in lst:
        o = is_operator(i)
        if o != 1 and o != 2 and o != 3 and o != 4:
            push(n, i)
        else:
            s = float(top(n))
            pop(n)
            f = float(top(n))
            pop(n)
            if o == 1:
                r = f + s
            elif o == 2:
                r = f - s
            elif o == 3:
                r = f * s
            elif o == 4:
                r = f / s
            push(n, r)
    return (top(n))
            

ans = postfixEval(exp)
print(ans)
