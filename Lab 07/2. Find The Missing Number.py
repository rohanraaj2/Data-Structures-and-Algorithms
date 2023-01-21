def findMissingNumber(powerTwoList, size):
 f = 0
 t = size - 1
 m = t // 2
 while f <= t:

 if f == size - 1:
 return (2 ** m)
 if m > -1 and powerTwoList[m] > (2 ** m):
 t = m - 1
 m = t // 2

 if m < (size - 1) and powerTwoList[m] == (2 ** m):
 f = m + 1
 m = f + ((t - f) // 2)
 #t = size - 1
 return (2 ** (f))
