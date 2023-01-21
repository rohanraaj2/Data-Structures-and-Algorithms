seq = input()

def isCorrect(seq):
    print(seq)
    l = len(seq)
    p = int(l / 2)
    w = 0
    t = '()'
    s = ''
    c1 = 0
    c2 = 0
          
    if l % 2 == 1:
        return 'No'
    elif seq == t * p:
        return 'Yes'
    else:
        for j in range(l):
            if seq[j] == '(':
                c1 += 1
            elif seq[j] == ')':
                c2 += 1
                if seq[j+1] != ')':
                    if c2 != c1:
                        w = 1
                        loc = j + 1
                        break
                    else:
                        c1 = 0
                        c2 = 0
    if w == 1:
        for i in range(l):
            if i <= l - 2 and seq[i] == ')' and seq[i+1] == '(':
                s+= seq[i+1]
                s+= seq[i]
                if s == t * p:
                    return 'Yes'
                else:
                    return 'No'
print(isCorrect(seq))
