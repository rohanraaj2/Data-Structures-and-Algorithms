seq = input()
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

def isCorrect(seq):
    s = []
    seq = '(' + seq + ')'
    l = len(seq)
    if l % 2 == 1:
        return 'No'
    else:
        for i in range(l):
            if seq[i] == '(':
                push (s, seq[i])
            else:
                if is_empty(s) == False:
                    pop(s)
                else:
                    return 'No'
    if is_empty(s) == True:
        return 'Yes'
    else:
        return 'No'
                    
print(isCorrect(seq))
