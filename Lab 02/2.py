s = input()

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
    
def string_reversal(s):
    r = ''
    l = []
    if type(s) == str:
        for i in s:
            push(l, i)
        while is_empty(l) == False:
            r += top(l)
            n = pop(l)
        return r

print(string_reversal(s))
