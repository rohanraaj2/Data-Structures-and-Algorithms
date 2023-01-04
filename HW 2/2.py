def BinaryInsertionSort(lst):
  n = len(lst)
  for i in range (1, n):
    val = lst[i]
    h = i - 1
    p = BinarySearch(lst, val, 0, h)
    for j in range (h, p - 1, -1):
        temp1 = lst[j + 1]
        lst[j + 1] = lst[j]
        lst[j] = temp1
        j = j - 1
    lst[p] = val
    i = i + 1
  return lst
