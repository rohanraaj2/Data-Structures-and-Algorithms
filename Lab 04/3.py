import ast
lst = input()
lst = ast.literal_eval(lst)
def InterLeaveQueue(lst):
    l = len(lst)
    h = int(l / 2)
    s = []
    for j in range(h, l):
        s.append (lst[j])
    for i in range(l):
        if i % 2 == 1:
            lst.insert(i, s[int((i-1)/2)])
            lst.pop(-1)
    return lst

print(InterLeaveQueue(lst))
