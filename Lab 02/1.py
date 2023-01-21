# Enter your code here. Read input from STDIN. Print output to STDOUT
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
