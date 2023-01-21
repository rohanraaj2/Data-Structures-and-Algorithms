import ast
student_records = input()
student_records = ast.literal_eval(student_records)
ID = input()
record_title = input()
data = input()
def binary_search_iterative(lst, item):
    import math
    l = len(lst) - 1
    m = math.ceil(l / 2)
    i = -1
    f = 0
    if lst [m] == item or lst[0] == item:
        return lst.index(item)
    while f < l and lst[m] < item:
        f = m + 1
        n = l - f
        m = f + math.ceil (n/2)
        if lst [f] == item or lst[m] == item:
            i = lst.index(item)
            return i
    while l > f and lst[m] > item:
        l = m - 1
        m = math.ceil(l/2)
        if lst[l] == item or lst [m] == item:
            i = lst.index(item)
    return i

def update_record(student_records, ID, record_title, data):
    if record_title == 'ID':
        return 'ID cannot be updated'
    else:
        lst = []
        for i in range(len(student_records)):
            lst.append(student_records[i][0])
        v = binary_search_iterative(lst, ID)
        if v == -1:
            return 'Record not found'
        else:
            if record_title == 'Email':
                student_records[v] = (student_records[v][0], data, student_records[v][2], student_records[v][3])
            elif record_title == 'Mid1':
                student_records[v] = (student_records[v][0], student_records[v][1], int(data), student_records[v][3])
            elif record_title == 'Mid2':
                student_records[v] = (student_records[v][0], student_records[v][1], student_records[v][2], int(data))
        return student_records

print(update_record(student_records, ID, record_title, data))
