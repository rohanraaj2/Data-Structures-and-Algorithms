def sort_abs_difference(lst, x):
 l = len(lst)
 d = max(lst)
 ld = []
 n = []
 for i in range(l):
 if abs(x - lst[i]) not in ld:
 ld.append(abs(x - lst[i]))
 ld.sort()
 for k in ld:
 for j in range(l):
 if abs(x - lst[j]) == k:
 n.append(lst[j])
 return n
