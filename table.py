list1=range(1,5)
list2=[]
list3=[]
for elem in list1:
    user=input('Your Name:')
    score=input('Your score:')
    list2.append(user)
    list3.append(score)
    print ("\n" * 5)
def yes():
    print('User Score')
    for a,b in zip(list2,list3):
        print(a,b)

list1=range(1,3)
list2=[]
list3=[]
for elem in list1:
    user=input('Your Name:')
    score=input('Your score:')
    list2.append(user)
    list3.append(score)
    print ("\n" * 1)
for a in list2:
  print(a,sep=" ",end='',flush=False)
for b in list3:
  print(a,sep=' ',end='',flush=False)





yes()



#Table code but better
list1=range(1,50)
iter1=iter(list1)
for elem in list1:
  print (iter1.__next__(),iter1.__next__(),sep=' ',end="",flush="true")


list1=range(1,3)
list2=[]
list3=[]
list4=[]
list5=[]
stat=1 
stat1=1
for elem in list1:
    user=input('Your Name:')
    score=str(input('Your score:'))
    list2.append(user)
    list3.append(score)
    print ("\n" * 1)
for elem in list2
  for t in elem:
    space=stat += 1
    list4.append(space)
for elem in list3:
  for q in elem:
    spacer=stat1 += 1
    list5.append(spacer)
iter1=iter(list4)
iter2=iter(list5)
for a in list2:
  print(a,sep=" ",end='',flush=False)
for b in list3:
  print(b,sep=' ',end='',flush=False)




list1=range(1,3)
list2=[]
list3=[]
list4=[]
list5=[]
stat=1 
stat1=1
for elem in list1:
    user=input('Your Name:')
    score=str(input('Your score:'))
    list2.append(user)
    list3.append(score)
    print ("\n" * 1)
for elem in list2:
  for t in elem:
    stat+=1
    space=stat + 1
    list4.append(space)
for elem in list3:
  for q in elem:
    stat1+=1
    spacer=stat1+1
    list5.append(spacer)
iter1=iter(list4)
iter2=iter(list5)

for a in list2:
  if iter1.__next__() < iter2.__next__():
    sspacer=iter2-iter1
  if iter1.__next__() > iter2.__next__():
    sspacer=iter1-iter2  
  print(a,sspacer,sep=" ",end='',flush=False)
for b in list3:
  print(b,sep=' ',end='',flush=False)
