def getTopIndex_UnimodelSequence(unimodel_sequence):
 l = len(unimodel_sequence) - 1
 m = l//2
 while unimodel_sequence[m] < unimodel_sequence[m + 1]:
 f = m + 1
 m = f + ((l - f) // 2)
 if unimodel_sequence[f] > unimodel_sequence[m]:
 return f
 return m
