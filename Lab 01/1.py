import ast
A = input()
A = ast.literal_eval(A)
B = input()
B = ast.literal_eval(B)
def matrix_subtraction(A,B):
    fl = []
    for i in range (len(A)):
        if len (A[i]) != len(B[i]):
            return ("Matrices A and B don't have the same dimension required for matrix subtraction.")
        else:
            l = []
            for j in range (len(A[i])):
                f = A[i][j] - B[i][j]
                l.append(f)
            fl.append(l)
    return (fl)
print(matrix_subtraction(A,B))
