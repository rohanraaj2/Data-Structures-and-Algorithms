import ast
rectangle_records = input()
rectangle_records = ast.literal_eval(rectangle_records)
record_title = input()
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
    return (lst)
        
def sort_rectangles(rectangle_records, record_title):
    n = []
    f = []
    for i in range(len(rectangle_records)):
        n.append(rectangle_records[i][record_title])
    insertion_sort(n)
    for j in range(len(rectangle_records)):
        for k in range(len(rectangle_records)):
            if rectangle_records[k][record_title] == n[j]:
                f.append(rectangle_records[k])
    return f
print(sort_rectangles(rectangle_records, record_title))
