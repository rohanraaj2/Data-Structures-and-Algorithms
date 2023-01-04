import ast
lst = input()
lst = ast.literal_eval(lst)

def bubble_sort(lst):
    l = len(lst) - 1
    if l == 0:
        print (lst)
    else:
        while l >= 1:
            for i in range(l):
                if lst[i] > lst[i + 1]:
                    temp = lst[i]
                    lst[i] = lst[i + 1]
                    lst[i + 1] = temp
            print (lst)
            l -= 1

bubble_sort(lst)
