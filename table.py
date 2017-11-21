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


