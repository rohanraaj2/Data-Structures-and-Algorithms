def smallest_absdiff_pairs(lst):
 lst.sort()
 d = lst[1] - lst[0]
 l = len(lst)
 m = []
 for i in range(l):
 if i < l - 1:
 if lst[i + 1] - lst[i] < d and lst[i + 1] - lst[i] != 0:
 d = lst[i + 1] - lst[i]
 m = []
 if lst[i + 1] - lst[i] == d and lst[i + 1] - lst[i] != 0:
 t = (lst[i], + lst[i + 1])
 m.append(t)
 return m
