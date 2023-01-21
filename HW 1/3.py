s=input()

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
        
def balanced_braces(s):
    stack = []
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    for i in s:
        if i in opening:
            push (stack, i)
        else:
            if is_empty(stack) == False:
                t = top(stack)
                p = opening.index(t)
                if i == closing[p]:
                    pop(stack)
            else:
                return False
    if is_empty(stack) == True:
        return True
    else:
        return False
    

print(balanced_braces(s))
