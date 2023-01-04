import ast
A = input()
A = ast.literal_eval(A)
B = input()
B = ast.literal_eval(B)
def matrix_multiplication(A,B):
    n = 0
    f = []
    if len (A[0]) != len (B):
        return ("The number of columns in Matrix A does not equal the number of rows in Matrix B required for Matrix Multiplication.")
    else:
        for k in range (len(A)):
                l = []
                for i in range (len(B[0])):
                    for j in range (len(A[k])):
                        n += A[k][j] * B[j][i]
                    l.append (n)
                    n = 0
                f.append(l)
        return f
        

print(matrix_multiplication(A,B))
