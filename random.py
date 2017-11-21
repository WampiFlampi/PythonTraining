for a,b in (list2,list3):
  print(a,b)
  a=range(1,5)
  iter1=iter(a)
  print (next(iter1))
  print (iter1.__next__())
