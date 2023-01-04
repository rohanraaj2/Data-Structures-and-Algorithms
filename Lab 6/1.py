import ast
lst = input()
lst = ast.literal_eval(lst)

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
        print (lst)

selection_sort(lst)
