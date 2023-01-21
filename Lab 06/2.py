import ast
lst = input()
lst = ast.literal_eval(lst)

def insertion_sort(lst):
    l = len(lst)
    c = 1
    while c < l: 
        for i in range(c, 0, - 1):
            n = lst[i]
            while n < lst[i - 1]:
                temp = n
                lst[i] = lst[i - 1]
                lst[i - 1] = temp
        c += 1
        print (lst)

insertion_sort(lst)
