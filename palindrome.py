#Homemade Palindrome Checker
b=0
a=input("a word:")
list1=[]
for elem in a:
    b=b+1
for elem in a:
    b=b-1
    q=a[b]
    list1.append(q)
list1=''.join(list1)
if a ==list1:
    print ("palindrome")
else:
    print ("sadness")





#Cheaty disgusting phil version
    
#a=input('any word:')
#x=a[::-1]
#if a==x:
    #print ('palindrome')
#else:
    #print ('sadness')
