exp = input()
def postfixEval(exp):
    lst = []
    j = 0
    lst = exp.split()
    while len(lst) > 1:
        f = j - 2
        s = j - 1
        if j < len(lst):
            if lst[j] == '+':
                r = float(lst[j - 2]) + float(lst[j - 1])
            elif lst[j] == '-':
                r = float(lst[j - 2]) - float(lst[j - 1])
            elif lst[j] == '*':
                r = float(lst[j - 2]) * float(lst[j - 1])
            elif lst[j] == '/':
                r = float(lst[j - 2]) / float(lst[j - 1])
            if lst[j] == '+' or lst[j] == '-' or lst[j] == '*' or lst[j] == '/':
                lst.pop(f)
                lst.pop(f)
                lst.pop(f)
                lst.insert(f, r)
                j = f
            j += 1
        else:
            j = 0
            
    return (float(lst[0]))
            

ans = postfixEval(exp)
print(ans)
