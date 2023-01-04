import ast
A = input()
A = ast.literal_eval(A)

def matrix_transpose(A):
    a = []
    b = []
    c = []
    d = []
    for i in range (len(A)):
        a.append(A[i][0])
        b.append(A[i][1])
        if len(A[i]) == 3: 
            c.append(A[i][2])
    d.append(a)
    d.append(b)
    if c != []:
        d.append(c)
    return d
print(matrix_transpose(A))
