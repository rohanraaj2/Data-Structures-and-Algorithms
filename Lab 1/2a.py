import ast
A = input()
A = ast.literal_eval(A)

def matrix_transpose(A):
    d = []
    for i in range (len(A[0])):
        a = []
        for j in range (len(A)):
            a.append(A[j][i])
        d.append (a)
    return d
print(matrix_transpose(A))
