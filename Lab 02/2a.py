s = input()

def push (lst, item):
    lst.append(item)
    
def pop(lst):
    return(lst[:-1])
    
def top(lst):
    return(lst[-1])

def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False
    
def string_reversal(s):
    r = ''
    if type(s) == str:
        while is_empty(s) == False:
            r += top(s)
            s = pop(s)
        return r
    
print(string_reversal(s))
