import ast
lst = input()
lst = ast.literal_eval(lst)
column = int(input())
def selection_sort(lst):
    l = len(lst)
    c = 0   
    while c < l:
        s = lst[c]
        for i in range(c, l):
            if s > lst[i]:
                s = lst[i]
                p = i
        if s != lst[c]:
            temp = lst [c]
            lst[c] = s
            lst[p] = temp
        c += 1
    return (lst)
def sort_matrix_by_columnNumber(lst, column):
    n = []
    f = []
    for i in range(len(lst)):
        n.append(lst[i][column])
    selection_sort(n)
    for j in range(len(lst)):
        for k in range(len(lst)):
            if lst[k][column] == n[j]:
                if lst[k] not in f:
                    f.append(lst[k])
    return f
        
print(sort_matrix_by_columnNumber(lst, column))
