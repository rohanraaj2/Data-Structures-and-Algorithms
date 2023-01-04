formula = input()
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
def inToPostFix (formula):
    postFixExpr = ''
    stack = []
    p = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}
    for i in formula:
        if i == '(':
            push (stack, i)
        elif i == ')':
            pop(stack)
            while i != '(':
                postFixExpr += i
                pop(stack)
        elif i == '+' or i == '-' or i == '*' or i == '/' or i == '//' or i == '%' or i == '&':
            if is_empty(stack) == False:
                t = top(stack)
            while not is_empty(stack) and (p[i] <= p[top(stack)]):
                tokenOut = pop(stack)
                postFixExpr += tokenOut
                t = top(stack)
            push (stack, i)
        else:
            postFixExpr += i
    while not is_empty(stack):
        pop(stack)
        postFixExpr += i
    return postFixExpr            
    
print(inToPostFix (formula))
