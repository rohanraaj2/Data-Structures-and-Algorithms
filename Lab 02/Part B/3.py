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

def enQueue(lst, data):
    lst.append(data)
    
def deQueue(lst):
    return(lst.pop(0))

def front(lst):
    return (lst[0])

def rear(lst):
    return (lst.pop())

def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False
    
def is_palindrome(s):
    if type(s) == str:
        n = ''
        s = s.lower()
        for j in s:
            if j.isalpha() == True:
                n += j
        stack = []
        queue = []
        for i in n:
            push(stack, i)
            enQueue(queue, i)
        while is_empty(stack) == False:
            if pop(stack) != deQueue(queue):
                return False
        return True
print(is_palindrome(s))
