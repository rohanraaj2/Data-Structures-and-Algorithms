expression = input()
def EvalutePrefix(expression):
    #operandStack = []
    operandStack = expression.split()
    c = 0
    f = ''
    s = ''
    while len(operandStack) > 1:
        if operandStack[c] != '+' and operandStack[c] != '-' and operandStack[c] != '*' and operandStack[c] != '/':
            j = int(operandStack[c])
            operandStack.insert(c, j)
        else:
            o = operandStack[c]
            f = operandStack[c + 1]
            s = operandStack[c + 2]
            while type(f) != int or type (s) != int:
                if operandStack[c + 1] != '+' and operandStack[c + 1] != '-' and operandStack[c + 1] != '*' and operandStack[c + 1] != '/':
                    f = int(operandStack[c + 1])
                else:
                    c += 1
                if operandStack[c + 2] != '+' and operandStack[c + 2] != '-' and operandStack[c + 2] != '*' and operandStack[c + 2] != '/':
                    s = int(operandStack[c + 2])
                    if type (f) != int:
                        f = operandStack[c + 1]
                else:
                    c += 2
                o = operandStack[c]
            for k in range(3):
                operandStack.pop(c)
            if o == '+':
                r = f + s
            elif o == '-':
                r = f - s
            elif o == '*':
                r = f * s
            elif o == '/':
                r = f / s
            operandStack.insert(c, r)
            c = -1
        c += 1
        
    
    return (operandStack[0])
    

print(EvalutePrefix(expression))
